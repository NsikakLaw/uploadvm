import sys
import re
import copy

counter=0

def increment_counter():
     global counter
     counter=counter+1
     return counter
# YOUR CODE GOES HERE
def reset_counter():
    global counter
    counter=0
    return counter

class Street(object):
    def __init__(self, name):
      self.name = name
      self.coordinates_list = []

    def add_coordinates(self,list1):
        for c  in range(0,len( list1)):
            self.coordinates_list.append(list1[c])

    def display_coordi(self):
        print self.coordinates_list

def converter(num):
    try:
        count_minus=0
        for c in num:
            if c!="0" and c!="1" and c!="2" and c!="3" and c!="4" and c!="5" and c!="6" and c!="7" and c!="8" and c!="9" and c!="-":
                return "error"
            elif c=="-":
                count_minus=count_minus+1
            if count_minus >1:
                return "error"
            try:
                ret = int(num)
            except ValueError:
                #Try float.
                return "error"
            if isinstance(ret,(int,long)):
                return ret
            else:
                return "error"
    except (ValueError,RuntimeError, TypeError, NameError):
        return "error"

def chk_street_name(street_name,list_obj):
    try:
        for a in range(0,len(list_obj)):
            if street_name.lower() == list_obj[a].name.lower():
                return a+1
        return False
    except (ValueError,RuntimeError, TypeError, NameError):
        return False

def return_single_list(lis):
    try:
        new_lis=[]
        newlist=[]
        for a in range (0,len(lis)):
            if isinstance(lis[a], list):
                for b in range(0,len(lis[a])):
                    if isinstance(lis[a][b], list):
                        for c in range(0,len(lis[a][b][c])):
                            if isinstance(lis[a][b],list):
                                return "error"
                            else:
                                new_lis.append(lis[a][b][c])
                    else:
                        new_lis.append(lis[a][b])
            else:
                new_lis.append(lis[a])
        for i in new_lis:
            if i not in newlist:
                newlist.append(i)
        return newlist
    except (ValueError,RuntimeError, TypeError, NameError):
        return "error"

def check_input(line):
    line=line.strip()
    if line[0] == "a" or line[0]=="c" or line[0]=="g" or line[0]=="r":
        try:
            if line[0]=="a":                                                 ###input check for command starting with a
                if len(line)==1:                                                   ### if input is only : a
                    return "errora"
                line1=line[1:]
                if line1[0]!=" ":
                    return "errora"                                              ###check for space after "a"
                line1=line1.strip()
                if line1[0]!="\"":
                    return "errora"                                                ###to check for quotes before street name
                line1=line1[1:]
                line1=line1.strip()
                street_name=""
                coordinate=""
                flag_street_name=True
                for c in line1:
                    if  flag_street_name and c!="\"":
                        street_name=street_name+ c
                    elif flag_street_name and c=="\"":
                        flag_street_name=False
                    elif not flag_street_name and c=="\"":
                        return "errora"
                    else:
                        coordinate=coordinate+c                                      ### to abstract street name and coordinates
                if street_name=="" or coordinate=="":
                    return "errora"
                for char in street_name:
                    bool= char.isalpha()
                    if char !=" ":
                        if not bool:
                            return "errora"
                list_coordinate=[]
                xy=""
                flag_coordinate=False
                count_coordinate=0
                count_comma=0
                list_object=[]
                if coordinate[0]!=" ":
                    return "errora"
                coordinate=coordinate.strip()
                if coordinate[0]!="(":
                    return "errora"
                if coordinate[0]!="(":
                    return "errora"
                for c in coordinate:
                    if c!="(" and c!=")" and c!="," and c!=" " and c!="1"  and c!="2" and c!="3" and c!="4" and c!="5" and c!="6" and c!="7" and c!="8" and c!="9" and c!="0" and c!="-":
                        return "errora"
                    elif c==" ":
                        continue
                    elif c=="(" and not flag_coordinate:
                        flag_coordinate=True
                        count_comma=0
                    elif c=="(" and flag_coordinate:
                        return "errora"
                    elif c==")" and not flag_coordinate:
                        return "errora"
                    elif flag_coordinate and c!="(" and c!=")" and c!="," :
                        xy=xy+c
                    elif flag_coordinate and c=="," and count_comma==0:
                        x=converter(xy)
                        if x=="error":
                            return "errora"
                        count_comma=count_comma+1
                        xy=""
                    elif flag_coordinate and count_comma==1 and c==")":
                        y=converter(xy)
                        if y=="error":
                            return "errora"
                        xy=""
                        list_object.append(x)
                        flag_coordinate=False
                        list_object.append(y)
                        list_object.append(street_name)
                        for a in list_coordinate:
                            if list_object==a:
                                return "errora"
                        count_coordinate=count_coordinate+1
                        list_coordinate.append(list_object)
                        list_object=[]
                    else:
                        return "errora"
                if count_coordinate>1 and not flag_coordinate:
                    return list_coordinate
                else:
                    return "errora"

            elif line[0]=="r":
                if len(line)==1:
                    return "errorr"
                line1=line[1:]
                if line1[0]!=" ":
                    return "errorr"
                line1=line1.strip()
                if line1[0]!="\"":
                    return "errorr"
                line1=line1[1:]
                line1=line1.strip()
                street_name=""
                extra=""
                flag_street_name=True
                for c in line1:
                    if  flag_street_name and c!="\"":
                        street_name=street_name+ c
                    elif flag_street_name and c=="\"":
                        flag_street_name=False
                    elif not flag_street_name and c=="\"":
                        return "errorr"
                    else:
                        extra=extra + c
                if street_name=="":
                    return "errorr"
                extra=extra.strip()
                if extra !="":
                    return "errorr"
                else:
                     return street_name
            elif line[0]=="c":
                if len(line)==1:
                    return "errorc"
                line1=line[1:]
                if line1[0]!=" ":
                    return "errorc"
                line1=line1.strip()
                if line1[0]!="\"":
                    return "errorc"
                line1=line1[1:]
                line1=line1.strip()
                street_name=""
                coordinate=""
                flag_street_name=True
                for c in line1:
                    if  flag_street_name and c!="\"":
                        street_name=street_name+ c
                    elif flag_street_name and c=="\"":
                        flag_street_name=False
                    elif not flag_street_name and c=="\"":
                        return "errorc"
                    else:
                        coordinate=coordinate+c
                if street_name=="" or coordinate=="":
                    return "errorc"
                for char in street_name:
                    bool= char.isalpha()
                    if char !=" ":
                        if not bool:
                            return "errorc"
                if coordinate[0]!=" ":
                    return "errorc"
                list_coordinate=[]
                xy=""
                list_object=[]
                flag_coordinate=False
                count_coordinate=0
                count_comma=0
                coordinate=coordinate.strip()
                if coordinate[0]!="(":
                    return "errorc"
                for c in coordinate:
                    if c!="(" and c!=")" and c!="," and c!=" " and c!="1"  and c!="2" and c!="3" and c!="4" and c!="5" and c!="6" and c!="7" and c!="8" and c!="9" and c!="0" and c!="-":
                        return "errorc"
                    elif c==" ":
                        continue
                    elif c=="(" and not flag_coordinate:
                        flag_coordinate=True
                        count_comma=0
                    elif c=="(" and flag_coordinate:
                        return "errorc"
                    elif c==")" and not flag_coordinate:
                        return "errorc"
                    elif flag_coordinate and c!="(" and c!=")" and c!="," :
                        xy=xy+c
                    elif flag_coordinate and c=="," and count_comma==0:
                        x=converter(xy)
                        if x=="error":
                            return "errorc"
                        count_comma=count_comma+1
                        xy=""
                    elif flag_coordinate and count_comma==1 and c==")":
                        y=converter(xy)
                        if y=="error":
                            return "errorc"
                        xy=""
                        list_object.append(x)
                        flag_coordinate=False
                        list_object.append(y)
                        list_object.append(street_name)
                        for a in list_coordinate:
                            if list_object==a:
                                return "errorc"
                        count_coordinate=count_coordinate+1
                        list_coordinate.append(list_object)
                        list_object=[]
                    else:
                        return "errorc"
                if count_coordinate>1 and not flag_coordinate:
                    return list_coordinate
                else:
                    return "errorc"
                return line1
            elif line[0]=="g":
                line1=line[1:]
                line1=line1.strip()
                if line1=="":
                    pass
                else:
                    return "errorg"
        except (ValueError,RuntimeError, TypeError, NameError):
            return "error"
    else :
        return "error"

def check_intersection(coor1,coor2,coor3and4):
    #try:
        ls=[]
        coor1[0]=float(coor1[0])     ###changeeeeeeeeeeeeeeeeeee
        coor2[0]=float(coor2[0])
        coor1[1]=float(coor1[1])
        coor2[1]=float(coor2[1])
        coor3and4[0][0]=float(coor3and4[0][0])
        coor3and4[0][1]=float(coor3and4[0][1])
        coor3and4[1][0]=float(coor3and4[1][0])
        coor3and4[1][1]=float(coor3and4[1][1])
        if coor1[0]<=coor2[0]:
            x1=coor1[0]
            y1=coor1[1]
            x2=coor2[0]
            y2=coor2[1]
        else:
            x1=coor2[0]
            y1=coor2[1]
            x2=coor1[0]
            y2=coor1[1]
        if coor3and4[0][0]<=coor3and4[1][0]:
            x3=coor3and4[0][0]
            y3=coor3and4[0][1]
            x4=coor3and4[1][0]
            y4=coor3and4[1][1]
        else:
            x3=coor3and4[1][0]
            y3=coor3and4[1][1]
            x4=coor3and4[0][0]
            y4=coor3and4[0][1]
        if (x1==x3) and (y1==y3) and (x2==x4) and (y2==y4):
            return "error"                                ###chk it*************
        if (x1==x4) and (y1==y4) and (x2==x3) and (y2==y3):
            return "error"                                  ###chk it***************
        if (x1==x3 and y1==y3) :
            return False
        elif (x1==x4 and y1== y4):
            return False
        elif (x2==x3 and y2==y3):
            return False
        elif (x2== x4 and y2== y4):
            return False
        if x2-x1 !=0:
            m12= (float(y2)-float(y1))/(x2-x1)
        else:
            m12="infinite"
        if x4-x3 !=0:
            m34=(float(y4)-float(y3))/(x4-x3)
        else:
            m34="infinite"
        if m12 !="infinite":
            c12=float(y1-(m12 * x1))
        if m34 !="infinite":
            c34 = float( y3-(m34 * x3))
        if m12 !="infinite" and m34 !="infinite" :
            if(m34-m12==0):
                return False
            else:
                x=float((c34-c12)/(m12-m34))
                y=float((m12 * x) + c12)
                ###y=float("{0:.2f}".format(y))
                ###x=float("{0:.2f}".format(x))
                ls.append(x)
                ls.append(y)
                smally1=min(y1,y2)
                bigy1=max(y1,y2)
                smally2=min(y3,y4)
                bigy2=max(y3,y4)
                if (x >= x1 and x <= x2) and (x >= x3 and x <= x4) and (y >= smally1 and y<= bigy1) and (y >= smally2 and y<= bigy2):
                    return ls
                else:
                    return False
        elif m12 =="infinite" and m34=="infinite":
            return False
        else:
            if m12=="infinite":
                x=x1
                y=float((m34 * x) + c34)
                ###y=float("{0:.2f}".format(y))
                ls.append(x)
                ls.append(y)
                smally1=min(y1,y2)
                bigy1=max(y1,y2)
                smally2=min(y3,y4)
                bigy2=max(y3,y4)
                if (x >= x3 and x<= x4 ) and (y >= smally1 and y<= bigy1) and (y >= smally2 and y<= bigy2):
                    return ls
                else:
                    return False
            elif m34=="infinite":
                x=x3
                y=float( (m12 * x) + c12)
                ###y=float("{0:.2f}".format(y))
                ls.append(x)
                ls.append(y)
                smally1=min(y1,y2)
                bigy1=max(y1,y2)
                smally2=min(y3,y4)
                bigy2=max(y3,y4)
                if (x >= x1 and x<= x2 ) and (y >= smally1 and y<= bigy1) and (y >= smally2 and y<= bigy2):
                    return ls
                else:
                    return False
#    except (ValueError,RuntimeError, TypeError, NameError):
#        return "error"

def find_intersection(list_coor1,edges_list):
    #try:
        list3=[]
        if not edges_list:
            for a in range(0,len(list_coor1)-1):
                lass=[]
                lass.append(list_coor1[a])
                lass.append(list_coor1[a+1])
                edges_list.append(lass)
            return list3
        else:
            b=0
            while(b<=len(edges_list)-1):

                for a in range(0,len(list_coor1)-1):
                    #print list_coor1[a]
                    #print list_coor1[a+1]
                    #for k in range(0,len(edges_list)):
                    #    print edges_list[k]
                    if float(list_coor1[a][0])==float(edges_list[b][0][0]) and float(list_coor1[a][1])==float(edges_list[b][0][1]) and (float(list_coor1[a+1][0])!=float(edges_list[b][1][0]) or float(list_coor1[a+1][1])!=float(edges_list[b][1][1])):
                        if list_coor1[a][3]=="n" and list_coor1[a+1][3]=="n":
                            edges_list[b][0][3]="i"
                            list_name=[]
                            list_name_sub=[]
                            list_final=[]
                            list_name.append(edges_list[b][0][2])
                            list_name.append(list_coor1[a][2])
                            list_name_sub=copy.deepcopy(list_name)
                            list_name=return_single_list(list_name)
                            if list_name=="error":
                                list_name=list_name_sub
                            edges_list[b][0][2]=list_name
                            list_coor1[a]=copy.deepcopy(edges_list[b][0])
                            list_final.append(list_coor1[a])
                            list_final.append(list_coor1[a+1])
                            edges_list.append(list_final)
                    elif float(list_coor1[a][0])==float(edges_list[b][1][0]) and float(list_coor1[a][1])==float(edges_list[b][1][1]) and (float(list_coor1[a+1][0])!=float(edges_list[b][0][0]) or float(list_coor1[a+1][1])!=float(edges_list[b][0][1])):
                        if list_coor1[a][3]=="n" and list_coor1[a+1][3]=="n":
                            edges_list[b][1][3]="i"
                            list_name=[]
                            list_name_sub=[]
                            list_final=[]
                            list_name.append(edges_list[b][1][2])
                            list_name.append(list_coor1[a][2])
                            list_name_sub=copy.deepcopy(list_name)
                            list_name=return_single_list(list_name)
                            if list_name=="error":
                                list_name=list_name_sub
                            edges_list[b][1][2]=list_name
                            list_coor1[a]=copy.deepcopy(edges_list[b][1])
                            list_final.append(list_coor1[a])
                            list_final.append(list_coor1[a+1])
                            edges_list.append(list_final)
                    elif float(list_coor1[a+1][0])==float(edges_list[b][1][0]) and float(list_coor1[a+1][1])==float(edges_list[b][1][1]) and (float(list_coor1[a][0])!=float(edges_list[b][0][0]) or float(list_coor1[a][1])!=float(edges_list[b][0][1])):

                        if list_coor1[a][3]=="n" and list_coor1[a+1][3]=="n":
                            edges_list[b][1][3]="i"
                            list_name=[]
                            list_name_sub=[]
                            list_final=[]
                            list_name.append(edges_list[b][1][2])
                            list_name.append(list_coor1[a+1][2])
                            list_name_sub=copy.deepcopy(list_name)
                            list_name=return_single_list(list_name)
                            if list_name=="error":
                                list_name=list_name_sub
                            edges_list[b][1][2]=list_name
                            list_coor1[a+1]=copy.deepcopy(edges_list[b][1])
                            list_final.append(list_coor1[a])
                            list_final.append(list_coor1[a+1])
                            edges_list.append(list_final)
                    elif float(list_coor1[a+1][0])==float(edges_list[b][0][0]) and float(list_coor1[a+1][1])==float(edges_list[b][0][1]) and (float(list_coor1[a][0])!=float(edges_list[b][1][0]) or float(list_coor1[a][1])!=float(edges_list[b][1][1])):

                        if list_coor1[a][3]=="n" and list_coor1[a+1][3]=="n":
                            edges_list[b][0][3]="i"
                            list_name=[]
                            list_name_sub=[]
                            list_final=[]
                            list_name.append(edges_list[b][0][2])
                            list_name.append(list_coor1[a+1][2])
                            list_name_sub=copy.deepcopy(list_name)
                            list_name=return_single_list(list_name)
                            if list_name=="error":
                                list_name=list_name_sub
                            edges_list[b][0][2]=list_name
                            list_coor1[a+1]=copy.deepcopy(edges_list[b][0])
                            list_final.append(list_coor1[a])
                            list_final.append(list_coor1[a+1])
                            edges_list.append(list_final)
                    elif float(list_coor1[a+1][0])==float(edges_list[b][0][0]) and float(list_coor1[a+1][1])==float(edges_list[b][0][1]) and (float(list_coor1[a][0])==float(edges_list[b][1][0]) and float(list_coor1[a][1])==float(edges_list[b][1][1])):
                        if list_coor1[a][3]=="n" and list_coor1[a+1][3]=="n":
                            edges_list[b][0][3]="i"
                            edges_list[b][1][3]="i"
                            list_name=[]
                            list_name_sub=[]
                            list_final=[]
                            list_name.append(edges_list[b][0][2])
                            list_name.append(list_coor1[a+1][2])
                            list_name_sub=copy.deepcopy(list_name)
                            list_name=return_single_list(list_name)
                            if list_name=="error":
                                list_name=list_name_sub
                            edges_list[b][0][2]=list_name
                            edges_list[b][1][2]=list_name
                            list_coor1[a+1]=copy.deepcopy(edges_list[b][0])
                            #list_final.append(list_coor1[a])
                            #list_final.append(list_coor1[a+1])
                    elif float(list_coor1[a+1][0])==float(edges_list[b][1][0]) and float(list_coor1[a+1][1])==float(edges_list[b][1][1]) and (float(list_coor1[a][0])==float(edges_list[b][0][0]) and float(list_coor1[a][1])==float(edges_list[b][0][1])):

                        if list_coor1[a][3]=="n" and list_coor1[a+1][3]=="n":
                            edges_list[b][0][3]="i"
                            edges_list[b][1][3]="i"
                            list_name=[]
                            list_name_sub=[]
                            list_final=[]
                            list_name.append(edges_list[b][0][2])
                            list_name.append(list_coor1[a][2])
                            list_name_sub=copy.deepcopy(list_name)
                            list_name=return_single_list(list_name)
                            if list_name=="error":
                                list_name=list_name_sub
                            edges_list[b][0][2]=list_name
                            list_coor1[a]=copy.deepcopy(edges_list[b][0])
                            #list_final.append(list_coor1[a])
                            #list_final.append(list_coor1[a+1])
                    else:

                        flag=check_intersection(list_coor1[a],list_coor1[a+1],edges_list[b])
                        if flag==False and b==len(edges_list)-1:                                             ###at the end
                            flag_edge_chk1=True
                            for m in range(0,len(edges_list)):
                                if float(list_coor1[a][0])==float(edges_list[a][0][0]) and float(list_coor1[a][1])==float(edges_list[m][0][1]) and float(list_coor1[a+1][0])==float(edges_list[m][1][0]) and float(list_coor1[a+1][1])==float(edges_list[m][1][1]):
                                    if list_coor1[a][3]=="n" and list_coor1[a+1][3]=="n":
                                        pass
                                    else:
                                        del edges_list[m]
                                        break
                            #if flag_edge_chk1:
                            #    lass=[]
                            #    lass.append(list_coor1[a])
                            #    lass.append(list_coor1[a+1])
                            #    edges_list.append(lass)
                        elif flag==False:                                                                  ###still to check other edges
                            continue
                        elif flag=="error":
                            pass
                        else:
                            ls=flag
                            flag_inter=True
                            if (ls[0]!=float(list_coor1[a][0]) or ls[1]!=float(list_coor1[a][1])) and (ls[0]!=float(list_coor1[a+1][0]) or ls[1]!=float(list_coor1[a+1][1])) and (ls[0]!=float(edges_list[b][0][0]) or ls[1]!=float(edges_list[b][0][1])) and (ls[0]!=float(edges_list[b][1][0]) or ls[1]!=float(edges_list[b][1][1])):
                                edge1=[]
                                edge2=[]
                                new_coor=[]
                                list_name=[]
                                list_name_sub=[]
                                for l in range(0,len(ls)):
                                    new_coor.append(ls[l])
                                list_name.append(edges_list[b][0][2])
                                list_name.append(list_coor1[a][2])
                                list_name_sub=copy.deepcopy(list_name)
                                list_name=return_single_list(list_name)
                                if list_name=="error":
                                    list_name=list_name_sub
                                new_coor.append(list_name)
                                new_coor.append("i")
                                edge1.append(edges_list[b][0])
                                edge1.append(new_coor)
                                edge2.append(new_coor)
                                edge2.append(edges_list[b][1])
                                #edges_list.append(edge1)
                                #edges_list.append(edge2)
                                del edges_list[b]
                                edges_list.insert(b,edge1)
                                edges_list.insert(b+1,edge2)
                                list_coor1.insert(a+1,new_coor)
                            elif (ls[0]!=float(list_coor1[a][0]) or ls[1]!=float(list_coor1[a][1])) and (ls[0]!=float(list_coor1[a+1][0]) or ls[1]!=float(list_coor1[a+1][1])) and ((ls[0]==float(edges_list[b][0][0]) and ls[1]==float(edges_list[b][0][1])) or (ls[0]==float(edges_list[b][1][0]) and ls[1]==float(edges_list[b][1][1]))):

                                new_coor=[]
                                list_name=[]
                                list_name_sub=[]
                                if ls[0]==float(edges_list[b][0][0]) and ls[1]==float(edges_list[b][0][1]):
                                    for l in range(0,len(ls)):
                                        new_coor.append(ls[l])
                                    list_name.append(edges_list[b][0][2])
                                    list_name.append(list_coor1[a][2])
                                    list_name_sub=copy.deepcopy(list_name)
                                    list_name=return_single_list(list_name)
                                    if list_name=="error":
                                        list_name=list_name_sub
                                    new_coor.append(list_name)
                                    new_coor.append("i")
                                    edges_list[b][0][3]="i"
                                elif ls[0]==float(edges_list[b][1][0]) and ls[1]==float(edges_list[b][1][1]):
                                    for l in range(0,len(ls)):
                                        new_coor.append(ls[l])
                                    list_name.append(edges_list[b][1][2])
                                    list_name.append(list_coor1[a][2])
                                    list_name_sub=copy.deepcopy(list_name)
                                    list_name=return_single_list(list_name)
                                    if list_name=="error":
                                        list_name=list_name_sub
                                    new_coor.append(list_name)
                                    new_coor.append("i")
                                    edges_list[b][1][3]="i"
                                list_coor1.insert(a+1,new_coor)
                            elif ((ls[0]==float(list_coor1[a][0]) and ls[1]==float(list_coor1[a][1])) or (ls[0]==float(list_coor1[a+1][0]) and ls[1]==float(list_coor1[a+1][1]))) and ((ls[0]!=float(edges_list[b][0][0]) or ls[1]!=float(edges_list[b][0][1])) and (ls[0]!=float(edges_list[b][1][0]) or ls[1]!=float(edges_list[b][1][1]))):

                                new_coor=[]
                                edge1=[]
                                edge2=[]
                                list_name=[]
                                list_name_sub=[]
                                if ls[0]==float(list_coor1[a][0]) and ls[1]==float(list_coor1[a][1]):
                                    for l in range(0,len(ls)):
                                        new_coor.append(ls[l])
                                    list_name.append(edges_list[b][0][2])
                                    list_name.append(list_coor1[a][2])
                                    list_name_sub=copy.deepcopy(list_name)
                                    list_name=return_single_list(list_name)
                                    if list_name=="error":
                                        list_name=list_name_sub
                                    new_coor.append(list_name)
                                    new_coor.append("i")
                                    edge1.append(edges_list[b][0])
                                    edge1.append(new_coor)
                                    edge2.append(new_coor)
                                    edge2.append(edges_list[b][1])
                                    del edges_list[b]
                                    edges_list.append(edge1)
                                    edges_list.append(edge2)
                                    list_coor1[a][2]=copy.deepcopy(list_name)
                                    list_coor1[a][3]="i"
                                elif ls[0]==float(list_coor1[a+1][0]) and ls[1]==float(list_coor1[a+1][1]):
                                    for l in range(0,len(ls)):
                                        new_coor.append(ls[l])
                                    list_name.append(edges_list[b][0][2])
                                    list_name.append(list_coor1[a+1][2])
                                    list_name_sub=copy.deepcopy(list_name)
                                    list_name=return_single_list(list_name)
                                    if list_name=="error":
                                        list_name=list_name_sub
                                    new_coor.append(list_name)
                                    new_coor.append("i")
                                    edge1.append(edges_list[b][0])
                                    edge1.append(new_coor)
                                    edge2.append(new_coor)
                                    edge2.append(edges_list[b][1])
                                    del edges_list[b]
                                    edges_list.append(edge1)
                                    edges_list.append(edge2)
                                    list_coor1[a+1][2]=copy.deepcopy(list_name)
                                    list_coor1[a+1][3]="i"

                b=b+1
        for p in range(0,len(list_coor1)-1):
            lass=[]
            lass.append(list_coor1[p])
            lass.append(list_coor1[p+1])
            edges_list.append(lass)
        return True
    #except (ValueError,RuntimeError, TypeError, NameError):
    #    return "error"

def print_vertices_and_edges(vertices,edges):
    print "V = {"
    for b in range(0,len(vertices)):
        ###if (vertices[b][0]-int(vertices[b][0]))==0.00:
        ###    vertices[b][0]=int(vertices[b][0])
        ###if (vertices[b][1]-int(vertices[b][1]))==0.00:
        ###    vertices[b][1]=int(vertices[b][1])
        q1=str(vertices[b][2])
        q2=str(round(vertices[b][0],2))
        q3=str(round(vertices[b][1],2))
        print  "%s :   (%s,%s)" %(q1,q2,q3)
        ###print('{0:2d}: ({2:.2f},{2:.2f})'.format(b, float(vertices[b][0]), float(vertices[b][1]) ))
    print "}"
    print_edges=[]
    for l in range(0,len(edges)):
        ls=[]
        for m in range(0, len(vertices)):
            if float(edges[l][0][0])==float(vertices[m][0]) and float(edges[l][0][1])==float(vertices[m][1]):
                ls.append(vertices[m][2])
        for n in range(0,len(vertices)):
            if float(edges[l][1][0])==float(vertices[n][0]) and float(edges[l][1][1])==float(vertices[n][1]):
                ls.append(vertices[n][2])
        print_edges.append(ls)

    for t in range(0,len(print_edges)-1):
        for p in range(t+1,len(print_edges)):
            if (print_edges[t][0]==print_edges[p][0]) and (print_edges[t][1]==print_edges[p][1]):
                del print_edges[t]
            elif (print_edges[t][0]==print_edges[p][1]) and (print_edges[t][1]==print_edges[p][0]):
                del print_edges[t]

    print "E = {"
    for b in range(0,len(print_edges)):
        w1=str(print_edges[b][0])
        w2=str(print_edges[b][1])
        if b!= len(print_edges)-1:
            print "<%s,%s>,"%(w1,w2)
        elif b== len(print_edges)-1:
            print "<%s,%s>"%(w1,w2)
    print "}"



def display_vertices_and_edges(list_edges,vertices):
    vertices1=[]
    print_vertices=[]
    edges=[]
    print_edges=[]
    ##vertices
    for a in range(0,len(list_edges)):
        if(list_edges[a][0][3]=="i"  or list_edges[a][1][3]=="i" ):
            flag=True
            if float(list_edges[a][0][0]) ==float(list_edges[a][1][0]) and float(list_edges[a][0][1])==float( list_edges[a][1][1]):
                flag=False
                continue
            for b in range(0,len(vertices1)):
                if float(list_edges[a][0][0])==float(vertices1[b][0]) and float(list_edges[a][0][1])==float(vertices1[b][1]) :
                    flag=False
                    break
            if flag and len(vertices1)>0:
                vertices1.append(list_edges[a][0])
            flag=True
            for b in range(0,len(vertices1)):
                if float(list_edges[a][1][0])==float(vertices1[b][0]) and float(list_edges[a][1][1])==float(vertices1[b][1]) :
                    flag=False
                    break
            if flag and len(vertices1)>0:
                vertices1.append(list_edges[a][1])
            if not vertices1:
                vertices1.append(list_edges[a][0])
                vertices1.append(list_edges[a][1])
                ##edges
            if not edges:
                edges.append(list_edges[a])
            else:
                flag=True
                for b in range(0,len(edges)):
                    if float(list_edges[a][0][0])==float(edges[b][0][0]) and float(list_edges[a][0][1])==float(edges[b][0][1]) and float(list_edges[a][1][0])==float(edges[b][1][0]) and float(list_edges[a][1][1])==float(edges[b][1][1]):
                        flag=False
                if flag :
                    edges.append(list_edges[a])
    if not vertices:
        for s in range(0,len(vertices1)):
            ls=[]
            ls.append(vertices1[s][0])
            ls.append(vertices1[s][1])
            counter_vertices=increment_counter()
            ls.append(counter_vertices)
            print_vertices.append(ls)
    else:
        for l in range(0,len(vertices1)):
            for d in range(0,len(vertices)):
                if float(vertices1[l][0])==float(vertices[d][0]) and float(vertices1[l][1])==float(vertices[d][1]):
                    print_vertices.append(vertices[d])
                    continue
        for l in range(0,len(vertices1)):
            flag=False
            ls=[]
            for d in range(0,len(vertices)):
                if float(vertices1[l][0])==float(vertices[d][0]) and float(vertices1[l][1])==float(vertices[d][1]):
                    flag=True
                elif flag==False and d==len(vertices)-1 :
                    ls.append(vertices1[l][0])
                    ls.append(vertices1[l][1])
                    counter_vertices=increment_counter()
                    ls.append(counter_vertices)
                    print_vertices.append(ls)

    vertices=copy.deepcopy(print_vertices)

    print_vertices_and_edges(vertices,edges)
    return vertices

def main():
    ### YOUR MAIN CODE GOES HERE

    ### sample code to read from stdin.
    ### make sure to remove all spurious print statements as required
    ### by the assignment
    list_obj=[]
    list_edges=[]
    vertices=[]
    while True:
        line = sys.stdin.readline()
        if line == '':
            
            break
        #print 'read a line:', line
        if line =="\n":
            continue
        msg=check_input(line)
        if msg=="errora":
            print "Error: Input string in format : a \"street name\" (x1,y1) (x2,y2)..."
        elif msg=="errorr":
            print "Error: Input string in format : r \"street name\""
        elif msg=="errorc":
            print "Error: Input string in format : c \"street name\" (x1,y1) (x2,y2)..."
        elif msg=="errorg":
            print "Error: Input string in format : g"
        elif msg=="error":
            print "Error: Wrong command"
        else:
            line= line.strip()
            option=line[0]
            if option=="a":
                flag=True
                if list_obj:
                    for s in range(0,len(list_obj)):
                        for m in range(0,len(msg)):
                            if list_obj[s].name==msg[0][2]:
                                print "Error: street-name already exist"
                                flag=False
                                break
                        if not flag:
                            break
                flag1=False
                flag2=True
                if list_obj:
                    for t in range(0,len(list_obj)):
                        if len(list_obj[t].coordinates_list)==len(msg):
                            count_itr=0
                            for k in range(0,len(msg)-1):
                                if msg[k][0]==list_obj[s].coordinates_list[k][0] and msg[k][1]==list_obj[s].coordinates_list[k][1] and msg[k+1][0]==list_obj[s].coordinates_list[k+1][0] and msg[k+1][1]==list_obj[s].coordinates_list[k+1][1]:
                                    flag1=True
                                    count_itr+=1
                                if flag1 and count_itr==(len(msg)-1):
                                    flag2=False
                                    break
                    if not flag2:
                        print "Error: edges of two streets are same"
                        continue
                if not list_obj:
                    wer=reset_counter()
                if flag and not flag1:
                    obj=Street(msg[0][2])                  ###creating object
                    coor=[]
                    for m in range(0,len(msg)):
                        lst=[]
                        lst.append(msg[m][0])
                        lst.append(msg[m][1])
                        coor.append(lst)
                    obj.add_coordinates(coor)
                    list_obj.append(obj)
            elif option=="r":
                if list_obj:
                    chk=chk_street_name(msg,list_obj)
                    if chk!= False:
                        del list_obj[chk-1]
                    else:
                        print "Error: street not present"
                else:
                    print "Error: no streets added yet"
                    continue
                #for m in range(0,len(list_obj)):
                #    print list_obj[m].name
                #    print list_obj[m].coordinates_list

            elif option=="c":
                if list_obj:
                    chk=chk_street_name(msg[0][2],list_obj)

                    if chk!= False:
                        flag1=False
                        if not flag1:
                            del list_obj[chk-1]
                            obj=Street(msg[0][2])                  ###creating object
                            coor=[]
                            for m in range(0,len(msg)):
                                lst=[]
                                lst.append(msg[m][0])
                                lst.append(msg[m][1])
                                coor.append(lst)
                            obj.add_coordinates(coor)
                            list_obj.append(obj)
                    else:
                        print "Error: street not present"
                else:
                    print "Error: no streets added yet"
                    continue

                #for m in range(0,len(list_obj)):
                #    print list_obj[m].name
                #    print list_obj[m].coordinates_list
            elif option=="g":
                if list_obj:
                    list_edges=[]
                    for l in range(0,len(list_obj)):
                        msg=[]
                        for k in range(0,len(list_obj[l].coordinates_list)):
                            appender=[]
                            appender.append(list_obj[l].coordinates_list[k][0])
                            appender.append(list_obj[l].coordinates_list[k][1])
                            appender.append(list_obj[l].name)
                            appender.append("n")
                            msg.append(appender)
                        inter_list=find_intersection(msg,list_edges)
                        if inter_list=="error":
                            print "Error: fault in edges"
                    vertices=display_vertices_and_edges(list_edges,vertices)
                    #for q in range(0,len(list_obj)):
                    #    print list_obj[q].name
                            ###break
                    ###display_vertices_and_edges(list_edges,list_vertices)
                else:
                    print "Error: No streets present"
            else:
                continue
    ###print 'Finished reading input'
    # return exit code 0 on successful termination
    sys.exit(0)

if __name__ == '__main__':
    main()
