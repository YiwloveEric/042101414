import pandas as pd

def sort_20(address):
    """_summary_
    弹幕排序存储于excel文件
    Args:
        address (_type_): 文件地址
    """    
    df = pd.DataFrame()
    danmu_list = []
    count_list = []
    with open(f"{address}", encoding="utf-8") as f:
        for line in f.readlines():
            text = line.split("\t")
            danmu_list.append(text[0])
            count_list.append(int(text[1].strip()))
        df["弹幕"] = danmu_list
        df["次数"] = count_list
    df2 = df.sort_values("次数",ascending=False)
    df2.to_excel("排序后的弹幕.xlsx",index=False)

if __name__ == "__main__":
    sort_20("D:\\hadoop\\softwareoutput8\\part-r-00000")
