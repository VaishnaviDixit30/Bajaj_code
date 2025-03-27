def run(path) :     
    # import modules here 
    import pandas as pd 

    # logic
    path = "C:\\Users\\S42123\\Downloads\\Data Engineering\\Data Engineering\\data - sample.xlsx"
    df = pd.read_excel(path)
    
    # return your output
    return df

   
    count = {}

    for student_id, status in attendance:
        if status == 'Absent':
            if student_id in count:
                count[student_id] += 1 
            else:
                count[student_id] = 1  


    print(count)
