import pandas

excel_data_df = pandas.read_excel('stuffs.xlsx', sheet_name='Sheet1')
lst_date = excel_data_df['Date'].tolist()
lst_time = excel_data_df['Time'].tolist()
lst_importance = excel_data_df[0].tolist()
lst_stuffs = excel_data_df['Stuff'].tolist()

# print rows
for i in range(len(lst_date)):
    print(lst_date[i], lst_time[i],
          lst_importance[i], lst_stuffs[i])
# print whole sheet data
print(excel_data_df)
