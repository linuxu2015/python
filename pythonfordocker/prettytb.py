__author__ = 'Administrator'
def pt():
    from prettytable import PrettyTable
    a = PrettyTable(['creattime','labels','v_size','p_id','name','repodigests','id','size'])
    a.align['LABELS'] = 'l'
    a.padding_width = 1
    #for i in range(0,l_index):
        #print list_image[i]['RepoTags'][0]
    ima = 1
    createtime = 2
    ima_created = 1
    ima_labels = 1
    vsize = 1
    ima_vsize = 2
    ima_pid = 2
    ima_name = 2
    ima_digest = 2
    ima_id = 2
    ima_size = 2
    a.add_row([ima_created,ima_labels,ima_vsize,ima_pid,ima_name,ima_digest,ima_id,ima_size])
    print a
pt()