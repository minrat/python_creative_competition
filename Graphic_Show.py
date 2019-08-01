        # 引入matplotlib 图形库
        import matplotlib.pyplot as plt

        # 将处理结果按需拆解
        names = list(data.keys())
        values = list(data.values())

        # 选择显示图形
        fig, axs = plt.subplots(figsize=(12, 6))
        # matplotlib 支持中文
        plt.rcParams['font.sans-serif'] = ['SimHei']

        # matplotlib X,Y 轴名称
        plt.xlabel("关键词")
        plt.ylabel("PR值")

        # 通过柱状图进行统计显示(按需选择)
        axs.bar(names, values)
        # axs.scatter(names, values)
        # axs.plot(names, values)

        # 设置标题
        fig.suptitle('Jieba分词结果展示')

        # 显示
        plt.show()
