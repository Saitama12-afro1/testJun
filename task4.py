import pprint
a =  {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    }
b = {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    }
c = {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    }





def segment_creater(segment1, segment2, segment3, segment4):
    if segment3 <= segment1:
            if segment1 <= (right := segment4) <= segment2:
                return segment1,right
            elif segment4 > segment2:
                return segment1,segment2
    elif segment2 >= segment3 >= segment1 :
            if (right := segment4) <= segment2:
                return segment3,right
            elif segment4 > segment2:
                return segment3,segment2 # 1 5 9 10
    return 0

def connect_segment(segment1, segment2, segment3, segment4):
    if  segment1 <= segment3 <= segment2 :
        if segment4 <= segment2:
            return segment1,segment2
        if segment4 > segment2:
            return segment1, segment4
    if segment1 <= segment4 <= segment2:
        if segment3 < segment1:
            return segment3, segment2
    if segment3 <= segment1 and segment2 <= segment4:
        return segment3, segment4
    return 0
            
def con_mas(mas):
    buff = []
    super_new_time = []
    for i in mas:
        for j in mas[1:]:
            if i != 0 and j != 0 and i not in buff and j not in buff :
                a = connect_segment( i[0],i[1],j[0], j[1])
                print(i,j,a)
                if a != 0:
                    buff.append(i)
                    buff.append(j)
                    super_new_time.append(a)
                elif i not in super_new_time:
                    super_new_time.append(i)
    return super_new_time
            
def task4(data):
    lesson = data["data"]["lesson"]
    pupil = data["data"]["pupil"]
    tutor = data["data"]["tutor"]
    pupil = con_mas(pupil)
    new_time = []
    for i in range(0, len(pupil) - 1,2):
        new_time.append(segment_creater(lesson[0], lesson[1], pupil[i], pupil[i+1]))
    pprint.pprint(f"{new_time=}")
    super_new_time = con_mas(new_time)
    if len(new_time) > 2:

        new_time = super_new_time
    answer_time = []
    pprint.pprint(f"{super_new_time=}")
    for segment in new_time:
        if segment != 0:
            for j in range(0,len(tutor) - 1, 2):
                answer_time.append(segment_creater(segment[0], segment[1], tutor[j], tutor[j+1]))
    # print()
    # pprint.pprint(f"{tutor=}")
    # print()
    # pprint.pprint(f"{answer_time=}")
    
        
    sum = 0
    for i in answer_time:
        if i != 0:
            a = i[1] - i[0]
            sum += a
    return sum

print(task4(a))
             
