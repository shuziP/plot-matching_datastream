绘制实时数据流，并与样本库中标签类比做匹配。

/data/

ElectricDevices_TEST：数据库，含六个不同类型的样本标签以及该标签下的数据。

DataStream：实时数据流

------------------------------------------------------------------------------------

analysis.ipynb：分析数据种类。

plot_datastream.py 绘制数据流并在ElectricDevices_TEST中查找最相近的标签种类。匹配到完全一致样本时闪动提示。



![plot1](https://github.com/shuziP/plot-matching_datastream/blob/master/screenshot/plot1.png)

![plot3](https://github.com/shuziP/plot-matching_datastream/blob/master/screenshot/plot3.png)

![plot2](https://github.com/shuziP/plot-matching_datastream/blob/master/screenshot/plot2.png)

打印输出：末尾为当前数据流与标签库中的误差。

![print](https://github.com/shuziP/plot-matching_datastream/blob/master/screenshot/print.png)
