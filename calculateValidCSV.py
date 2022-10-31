import pandas as pd

MEMBERS = ["604", "605", "606", "607", "608", "609", "610", "611", "612", "613", "614", "615", "616", "617", "618", "619", "620", \
    "621", "622", "623", "624", "625", "627", "628", "629", "630", "631", "632" ,"633", "634", "635", "636", "637", "638", "639", \
    "641", "643", "644", "645", "650", "651", "652", "653"]

def calculate(sid):
    val_csv = "./val/" + "val" + sid + ".csv"
    cal_csv = "./val/res.csv"

    df = pd.read_csv(val_csv)
    df = df.replace(-1, 0)
    df = df.drop('date', axis=1)

    m_mean = df.iloc[:, 0:4].mean().mean()
    m_mean = str(m_mean.round(1))

    w_mean = df.iloc[:, 4:].mean().mean()
    w_mean = str(w_mean.round(1))

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
