target_column_name = 'TARGET'

target_dict = {'GRASS': 0,
               'PATH': 1,
               'WINDOW': 2,
               'CEMENT': 3,
               'FOLIAGE': 4,
               'SKY': 5,
               'BRICKFACE': 6}


def data_add_target(path_in, path_out):
    f_in = open(path_in, 'r')
    f_out = open(path_out, 'w')

    title = f_in.readline().rstrip()
    f_out.write(title + ',' + target_column_name + '\n')

    line = f_in.readline().rstrip()
    while line != '':
        target = target_dict[line.split(',')[0]]
        f_out.write(line + ',' + str(target) + '\n')
        line = f_in.readline().rstrip()
    f_in.close()
    f_out.close()


data_add_target('data/segmentation.data', 'data/segmentation_target.data')
data_add_target('data/segmentation.test', 'data/segmentation_target.test')
