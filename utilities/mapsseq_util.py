import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.cluster import hierarchy
from statsmodels.sandbox.stats.multicomp import multipletests
import scipy.stats as stats
import networkx as nx #networkx 1.11 required
import pygraphviz #pygraphviz 1.3.1 required
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib as mpl
import matplotlib.patches as patches

#### utility functions 

def calc_cutoff(df, r, part_input):
    fil=df.filter(regex=r)
    ordered=np.sort(np.array(fil.sum(axis=0)))[::-1]
    part_range = range(1,ordered.shape[0]+1)
    num_part = sum(ordered>(sum(ordered)/float(part_input)))
    min_reads = ordered[num_part]
    return num_part, min_reads

def return_raw_data(df, sname, part_input):
    r1 = '^'+sname+'r1'
    fil1=df.filter(regex=r1)
    _,min_reads1 = calc_cutoff(df, r1, part_input)
    fil1=fil1.T.loc[fil1.sum(0)>min_reads1] 

    r2 = '^'+sname+'r2'
    fil2=df.filter(regex=r2)
    _,min_reads2 = calc_cutoff(df, r2, part_input)
    fil2=fil2.T.loc[fil2.sum(0)>min_reads2]
    
    output = pd.concat([fil1, fil2])
    return output.T

def filt_data(df, sname, part_input = 2500, filter_clust = False, show_removed = False, \
    min_appearance = False, min_prop = 0, verb = False):
    output = return_raw_data(df, sname, part_input).T
    output = output.div(output.sum(1),axis=0)

    if filter_clust == True: 
        data = output.T
        num = data.shape[1]
        corr_mat = data.corr('pearson')>0.95
        link = hierarchy.linkage(corr_mat, method='average')
        thresh = 0.6*max(link[:, 2])
        clusters = hierarchy.fcluster(link, thresh, 'distance')

        c_drop = []
        for c in set(clusters):
            size = sum(clusters == c)
            r1_memb = sum([i.split(sname)[1][:2] == 'r1' for i in data.columns[clusters == c]])
            if size/float(num) > 0.01: #if cluster is greater than 1% of dataset
                if (r1_memb/float(size) < 0.1) or (r1_memb/float(size) > 0.9): #if cluster is dominated by one replicate
                    c_drop.append(c)

        output = data.T[[i not in c_drop for i in clusters]].T
        for i in set(c_drop): #adding back in one particle for each removed cluster
            first_instance_cluster = data.iloc[:,np.where(clusters == i)[0][0]]
            output = pd.concat([output, first_instance_cluster], axis =1)
        output = output.T
        if verb == True:
            print str(data.shape[1]-output.shape[0])+\
            ' particles removed during cluster filtering'

        if show_removed == True: 
            for c in c_drop:
                ax = plt.axes()
                removed_cluster = data.T[clusters == c].T
                removed_cluster =  removed_cluster.loc[((removed_cluster>0).sum(axis=1)>0),:]
                sns.heatmap(removed_cluster, cmap='Greys', ax = ax)
                ax.set_title('cluster '+str(c))

    if min_appearance == True:
        thresh = min_prop*output.shape[0]
        output=output.loc[:,((output>0).sum(axis=0)>thresh)]
    
    return output.T

#### plotting functions

def plot_filt_data(input_df, replicate_info = False, size = (4,4)):
    if replicate_info == True:
        colors=[]
        sname = input_df.columns[0].split('r1')[0]
        for i in input_df.columns:
            if sname+'r1' in i:
                colors.append('red')
            elif sname+'r2' in i:
                colors.append('black')
        sns.clustermap(input_df, col_colors=colors, cmap='Reds', figsize = size)
    else:
        sns.clustermap(input_df, cmap='Reds', figsize = size)

def plot_species_per_particle(input_df, xlim = [1,25]):
    data = input_df
    plt.figure(figsize=(3,3))
    plt.hist((data.T>0.02).sum(axis=1),bins=20,range=(0,20),normed=True, \
        histtype='stepfilled', facecolor="black",edgecolor='black')
    plt.xlim(xlim)
    plt.xlabel('# OTUs')
    plt.ylabel('prop. cell clusters')
    plt.tight_layout()
    plt.show()

#TO-DO cluster cannot be utilized with annot as the values are shuffled. Would need to custom reshuffle the annot matrix per the resulting clustering. 
def plot_association_heatmap(input_df, tax_map, ab_thresh=0.02, min_appearance = 0.1, size =(5,5), sig = 0.05, max_val = 2, num_part = 0):
    data = input_df
    if num_part > 0:
        data = data.T.sample(frac=(num_part/float(data.shape[1])), random_state = np.random.RandomState(seed=1)).T
    print 'number of clusters used is: '+str(data.shape[1])
    data=data.T>ab_thresh
    data=data.loc[:,((data>0).sum(axis=0)>(data.shape[0]*min_appearance))] 
    data=data.T.reindex(data.sum(axis=0).sort_values(ascending=False).index).T

    pvalue_a=[]
    or_a=[]
    for i in np.arange(1,data.shape[1]):
        for i2 in np.arange(i):
            table=pd.crosstab(data.T.iloc[i] > 0, data.T.iloc[i2] > 0)
            oddsratio,p_value=stats.fisher_exact(table, alternative = 'two-sided')
            pvalue_a.append(p_value)
            or_a.append(np.log2(oddsratio))
    #multiple testing correction
    _,pvalue_c,_,_=multipletests(pvalue_a,alpha=sig,method='fdr_bh')
    print str(np.sum([i<sig for i in pvalue_c])) + \
    ' significant associations detected, p<'+str(sig)+', FDR corrected'

    #reshape into matrix format
    mat_pv=np.zeros(shape=(data.shape[1],data.shape[1]))
    mat_or=np.zeros(shape=(data.shape[1],data.shape[1]))
    mat_sig= pd.DataFrame(index=data.T.index, columns=data.T.index)
    cnt=0
    for i in np.arange(1,data.shape[1]):
        for i2 in np.arange(i): 
            mat_pv[i,i2]=np.log10(pvalue_c[cnt])
            mat_or[i,i2]=or_a[cnt]
            if pvalue_c[cnt] < sig:
                mat_sig.iloc[i,i2] = str('x')
            else:
                mat_sig.iloc[i,i2] = str('')
            cnt+=1
    index_p=data.T.index
    to_plot=pd.DataFrame(mat_or+mat_or.T,index=index_p, columns=index_p)
    mat_sig = mat_sig.T.replace(np.NaN,'') + mat_sig.replace(np.NaN,'')

    label_map=[]
    for i in to_plot:
        if tax_map[0] in i:
            label_map=label_map+['#66c2a5']
        elif tax_map[1] in i:
            label_map=label_map+['#a6d854']
        elif tax_map[2] in i:
            label_map=label_map+['#8da0cb']
        elif tax_map[3] in i:
            label_map=label_map+['#e78ac3']
        elif tax_map[4] in i:
            label_map=label_map+['#fc8d62']
        elif tax_map[5] in i:
            label_map=label_map+['#ffd92f']
        elif tax_map[6] in i:
            label_map=label_map+['#e5c494']
        else:
            label_map=label_map+['#b3b3b3']

    sns.clustermap(to_plot,cmap='coolwarm',square=True, annot=mat_sig, \
        row_colors=label_map, fmt='', vmax = max_val, vmin = -1*max_val, \
        row_cluster=False, col_cluster=False, metric = 'braycurtis')

def plot_association_network(input_df, tax_map, net_pos = [], ab_thresh=0.02, min_appearance = 0.1, size = (5,5), sig = 0.05, max_val = 2, num_part=0, layout = 'circle'):
    data = input_df
    if num_part > 0:
        data = data.T.sample(frac=(num_part/float(data.shape[1])), random_state = np.random.RandomState(seed=1)).T
    print 'number of clusters used is: '+str(data.shape[1])
    data=data.T>ab_thresh
    data=data.loc[:,((data>0).sum(axis=0)>(data.shape[0]*min_appearance))] 
    data=data.T.reindex(data.sum(axis=0).sort_values(ascending=False).index).T

    pvalue_a=[]
    or_a=[]
    for i in np.arange(1,data.shape[1]):
        for i2 in np.arange(i):
            table=pd.crosstab(data.T.iloc[i] > 0, data.T.iloc[i2] > 0)
            oddsratio,p_value=stats.fisher_exact(table, alternative = 'two-sided')
            pvalue_a.append(p_value)
            or_a.append(np.log2(oddsratio))
    #multiple testing correction
    _,pvalue_c,_,_=multipletests(pvalue_a,alpha=sig,method='fdr_bh')
    print str(np.sum([i<sig for i in pvalue_c])) + \
    ' significant associations detected, p<'+str(sig)+', FDR corrected'

    #reshape into matrix format
    source_list=[]
    dest_list=[]
    or_val=[]
    cnt=0
    otu_label = [i.split('Otu')[1].split('_')[0] for i in data.columns]
    print otu_label
    for i in np.arange(1,data.shape[1]):
        for i2 in np.arange(i): 
            if pvalue_c[cnt] < sig:
                source_list.append(otu_label[i])
                dest_list.append(otu_label[i2])
                or_val.append(or_a[cnt])
            else:
                if layout == 'circle':
                    source_list.append(otu_label[i])
                    dest_list.append(otu_label[i2])
                    or_val.append(0)      
            cnt+=1
    
    added_nodes = set(source_list+dest_list)
    for i in otu_label:
        if i not in added_nodes:
            source_list.append(i)
            dest_list.append(i)
            or_val.append(0)
            
    df = pd.DataFrame({ 'from':source_list, 'to':dest_list})
    G=nx.from_pandas_dataframe(df, 'from', 'to', create_using=nx.Graph() )

    if layout == 'neato':
        pos = graphviz_layout(G, prog="neato") #neato, twopi, circo, dot
    if layout == 'circle':
        pos = nx.shell_layout(G,nlist=[net_pos])

    #calculate #occurences of each otu
    num_occurences = data.sum(axis=0)
    num_occurences = 800*num_occurences/max(num_occurences)
    num_occurences.index = otu_label
    num_occurences = num_occurences.reindex(G.nodes())

    #reorganize edges
    source_dist_list = [i+'_'+j for i,j in zip(source_list, dest_list)]
    edge_vals = pd.DataFrame(or_val, index = source_dist_list)
    edge_list = []
    for i in [i[0]+'_'+i[1] for i in G.edges()]:
        if i in source_dist_list:
            edge_list.append(i)
        else: 
            swapped_string = i.split('_')[1]+'_'+i.split('_')[0]
            edge_list.append(swapped_string)
    edge_vals = edge_vals.reindex(edge_list)

    #calculate color labels
    label_map=[]
    cnt=0
    for i in data.columns:
        if tax_map[0] in i:
            label_map.append(0)
        elif tax_map[1] in i:
            label_map.append(1)
        elif tax_map[2] in i:
            label_map.append(2)
        elif tax_map[3] in i:
            label_map.append(3)
        elif tax_map[4] in i:
            label_map.append(4)
        elif tax_map[5] in i:
            label_map.append(5)
        elif tax_map[6] in i:
            label_map.append(6)
        else:
            label_map.append(7)
        cnt+=1

    #note: this is hacky reindexing, might need to be refactored to refactor the colormap and labelmap if other 
    #tax are missing
    color_options = ['#66c2a5', '#a6d854', '#8da0cb', '#e78ac3','#fc8d62','#ffd92f','#e5c494','#b3b3b3']
    if 7 not in label_map:
        color_options = color_options[:7]

    cm = mpl.colors.ListedColormap(color_options) 
    label_map = pd.DataFrame(label_map, otu_label)
    label_map = label_map.reindex(G.nodes()).values.tolist()
    label_map = [i[0] for i in label_map]

    edge_width = np.absolute(edge_vals[0].values.tolist())
    edge_width_corrected = []
    edge_type = []
    for i in edge_width:
        if i > max_val:
            edge_width_corrected.append(max_val)
            edge_type.append('solid')
        elif i == 0:
            edge_width_corrected.append(1)
            edge_type.append('dotted')
        else: 
            edge_width_corrected.append(i)
            edge_type.append('solid')

    plt.figure(figsize=size)
    nx.draw(G, pos=pos, node_size=num_occurences, edge_color=edge_vals[0].values.tolist(), \
            edge_cmap = plt.cm.coolwarm, edge_vmin=-1*max_val, edge_vmax=max_val, \
            width = edge_width_corrected, node_color=label_map, cmap=cm, linewidths=1, \
            with_labels=True, font_size=10, style = edge_type)

    ax = plt.gca() # to get the current axis
    ax.collections[0].set_edgecolor("#ffffff") 
