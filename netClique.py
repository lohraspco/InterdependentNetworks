

'''
Created on Jul 15, 2017

'''
import networkx as nx
import matplotlib.pylab as plt
import itertools as it
import random
def draw_circle_around_clique(clique,coords):
    dist=0
    temp_dist=0
    center=[0 for i in range(2)]
    color=next(colors)
    for a in clique:
        for b in clique:
            temp_dist=(coords[a][0]-coords[b][0])**2+(coords[a][1]-coords[b][1])**2
            if temp_dist>dist:
                dist=temp_dist
                for i in range(2):
                    center[i]=(coords[a][i]+coords[b][i])/2
    rad=dist**0.5/2
    cir = plt.Circle((center[0],center[1]), radius=rad*1.3,fill=False,color=color,hatch=next(hatches))
    plt.gca().add_patch(cir)
    plt.axis('scaled')
    # return color of the circle, to use it as the color for vertices of the cliques
    return color

global colors, hatches
colors=it.cycle('bgrcmyk')# blue, green, red, ...
hatches=it.cycle('/\|-+*')


no = 36
# create a random graph
G=nx.gnp_random_graph(n=no,p=0.4)
# remember the coordinates of the vertices
#coords=nx.spring_layout(G)
coords=nx.circular_layout(G)



fig = plt.figure()
#draw the graph
nx.draw(G,pos=coords,edge_color='blue',node_color='red', with_labels=True,font_color='black')
fig.savefig('/home/manicbird/Dropbox/EclipseWorkSpace/fig'+str(no)+'.png')


subG = random.sample(range(no),12)
print(type(subG))
nodeshapes='so^>v<dph8'
nx.draw_networkx_nodes(G.subgraph(subG), pos=coords, node_color='red', linewidths=3, node_shape='<')
nx.draw_networkx_edges(G.subgraph(subG), pos=coords, edge_color='black', width=3)


drawCliques = False

if drawCliques:
    # remove "len(clique)>2" if you're interested in maxcliques with 2 edges
    cliques=[clique for clique in nx.find_cliques(G) if len(clique)>2]

    k=[len(x) for x in cliques]
    counter=0
    for clique in cliques:
        
        if (k[counter]==max(k)):
            
            print ("Clique length to appear: {} ".format(len(clique)))
            nx.draw_networkx_nodes(G.subgraph(clique), pos=coords, node_color='blue')
            nx.draw_networkx_edges(G.subgraph(clique), pos=coords, edge_color='black', width=2)
            break
            #nx.draw_networkx_nodes(G,pos=coords,nodelist=clique,node_color=draw_circle_around_clique(clique,coords))
        counter += 1
plt.show()
fig.savefig('/home/manicbird/Dropbox/EclipseWorkSpace/fig'+str(no)+'clique.png')
if __name__ == '__main__':
    pass
