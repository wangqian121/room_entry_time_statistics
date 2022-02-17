def pull_time_avg(filename):
    with open(filename, 'r',encoding='utf-8') as file_to_read:
        list0 = []
        while True:
            lines = file_to_read.readline()  # 整行读取数据
            if not lines:
                break
            item = [i for i in lines.split()]#空格拆分每行的每个字符
            list0.append(item[7])
            print(list0)

        pull_time_list = [n for n in list0 if int(n) > 500]
        print(len(list0))
        print(pull_time_list)
        if len(pull_time_list)>10:
            sum=0
            for i in pull_time_list[:10]:
                sum=sum+int(i)
                avg=sum/10

        else:
            avg=0
            print("不足10个数据，请至少拉流10次")
    return avg

if __name__ == '__main__':
    a=pull_time_avg("adb.txt")
    print(a)
    # shell_adb()