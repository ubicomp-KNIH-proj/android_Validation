import pandas as pd

MEMBERS = ["604", "605", "609", "610", "611", "612", "613", "615", "616", "617", "618", "620", \
        "621", "623", "624", "625", "627", "628", "629", "631", "632" ,"633", "634", "635", "636", "637", \
        "638", "639",  "641", "643", "644", "645", "650", "651", "652", "653"]


def calculate(sid):
    val_csv = "D:\KNIH_Val/val_1030_1116/" + sid + ".csv"
    print(val_csv)
    cal_csv = "D:\KNIH_Val/val_1030_1116/res.csv"

    df = pd.read_csv(val_csv)
    df = df.replace(-1, 0)
    df = df.drop('date', axis=1)


    m_mean = df.iloc[:, 0:4].mean().mean()
    m_mean = str(round(m_mean,1))
    # m_mean = str(m_mean.round(1))

    w_mean = df.iloc[:, 4:].mean().mean()
    w_mean = str(round(w_mean,1))
    # w_mean = str(w_mean.round(1))

    writer = open(cal_csv, "a+")
    # writer.write("SID" + ',' + "Mobile" + ',' + "Watch" + '\n')

    write_down_list = [sid, m_mean, w_mean]

    for i in range(0, 3):
        writer.write(write_down_list[i] + ',')
    writer.write('\n')

    writer.close()

for sid in MEMBERS:
    calculate(sid)
    print("-----DONE-----")



# MEMBERS = ["604", "605", "607", "608", "609", "610", "611", "612", "613", "615", "616", "617", "618", "620", \
#     "621", "622", "623", "624", "625", "627", "628", "629", "630", "631", "632" ,"633", "634", "635", "636", "637", "638", "639", \
#     "641", "643", "644", "645", "650", "651", "652", "653"]