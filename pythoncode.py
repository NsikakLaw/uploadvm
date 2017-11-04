from ast import literal_eval
import re
from itertools import combinations
from collections import defaultdict

import json
import ast
import atexit

def takeSecond(elem):
    return elem[1]

def takeFirst(elem):
    return elem[0]

def exit_handler():
    print 'My application is ending!'

atexit.register(exit_handler)

def ccw(A,B,C):
	return (C.y-A.y)*(B.x-A.x) > (B.y-A.y)*(C.x-A.x)

def intersect(A,B,C,D):
	return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

data_point=[]

def crosses(l1,l2):
    if not parallel(l1,l2):
        x = line_intersection(l1,l2)
        minx1 = min(l1[0][0],l1[1][0])
        maxx1 = max(l1[0][0],l1[1][0])
        if x[0] < minx1 or x[0] > maxx1:
            return False

        minx1 = min(l2[0][0],l2[1][0])
        maxx1 = max(l2[0][0],l2[1][0])
        if x[0] < minx1 or x[0] > maxx1:
            return False

        minx1 = min(l2[0][1],l2[1][1])
        maxx1 = max(l2[0][1],l2[1][1])
        if x[1] < minx1 or x[1] > maxx1:
            return False

        minx1 = min(l1[0][1],l1[1][1])
        maxx1 = max(l1[0][1],l1[1][1])
        if x[1] < minx1 or x[1] > maxx1:
            return False
        return True

    else:
        return False

def gradient(l):
    """Returns gradient 'm' of a line"""
    m = None
    # Ensure that the line is not vertical
    if l[0][0] != l[1][0]:
        m = (1./(l[0][0]-l[1][0]))*(l[0][1] - l[1][1])
    return m

def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def parallel(l1,l2):
    '''
    if gradient(l1) != gradient(l2):
        return False
    return True
    '''
    if gradient(l1) != gradient(l2):
        if gradient(l1) != None and gradient(l2) != None:
            return  isclose(gradient(l1),gradient(l2))
        else:
            return False
    return True


def intersect(l):
    """Returns intersect (b) of a line using the equation of
    a line in slope and intercepet form (y = mx+b)"""
    return l[0][1] - (gradient(l)*l[0][0])

def line_intersection(l1,l2):
    """Returns the intersection point (x,y) of two line segments. Returns False
    for parallel lines"""
    # Not parallel
    if not parallel(l1,l2):
        if gradient(l1) is not None and gradient(l2) is not None:
            x = (1./(gradient(l1) - gradient(l2))) * (intersect(l2) - intersect(l1))
            y = (gradient(l1)*x) + intersect(l1)
        else:
            if gradient(l1) is None:
                x = l1[0][0]
                y = (gradient(l2)*x) + intersect(l2)
            elif gradient(l2) is None:
                x = l2[0][0]
                y = (gradient(l1)*x) + intersect(l1)
        return round (x,2) , round(y,2)
    else:
        return False



vertice= []


vert =[]
vertice =[]
intersection=[]
intersection_list=defaultdict(list)


def check_vert():
    #read_file()

    global vertice
    global data_point
    global intersection
    global intersection_list
    #read_file()
    i=0

    while i < (len(data_point)-1):
        ii=0
        for data_points in data_point[i]:
            #print data_points,"data_points",data_point
            x1,y1= data_points

            try:
                temp= data_point[i]
                x2,y2 = temp[ii+1]

            except Exception as e:
                pass
            ii=ii+1
            k=0

            at=i+1
            while at < len(data_point):
                aa=0
                data_pointa=data_point[at]

                while aa < (len(data_point[at])-1):
                    data_pointss = data_pointa[aa]
                    x3,y3= data_pointss
                    x4,y4= data_pointa[aa+1]

                    l1 = ((x1,y1),(x2,y2))
                    l2=((x3,y3),(x4,y4))
                    a1=(x1,y1)
                    b1=(x2,y2)
                    c1=(x3,y3)
                    d1=(x4,y4)

                    if  a1==c1 or a1==d1 or b1==c1 or b1==d1:
                        vertice.append(a1)
                        vertice.append(b1)
                        vertice.append(c1)
                        vertice.append(d1)

                        if a1==c1:
                            vertice_l = a1
                            intersection.append(a1)
                        elif a1==d1:
                            vertice_l = d1
                            intersection.append(d1)
                        elif b1==c1:
                            vertice_l = c1
                            intersection.append(c1)
                        elif b1==d1:
                            vertice_l = b1
                            intersection.append(b1)
                        else:
                            sdf1=23

                        elem = a1,b1,c1,d1

                        intersection_list[vertice_l].append(elem)

                    if  crosses(l1,l2) is True :

                        vert= line_intersection(l1,l2)
                        #print "Vert",vert,crosses(l1,l2)
                        vertx,verty=vert
                        vertice_l =  vertx,verty
                        vertice.append(vertice_l)
                        intersection.append(vertice_l)
                        vertice.append(a1)
                        vertice.append(b1)
                        vertice.append(c1)
                        vertice.append(d1)

                        elem = a1,b1,c1,d1
                        #intersection_list.append(elem)
                        intersection_list[vertice_l].append(elem)
                        sd=1
                        vn=[]

                    else:
                        if parallel(l1,l2) is True:
                            m = gradient(l1)
                            if m is None:
                                if l1[0][0] == l2[0][0]:
                                    low_val1 = min(l1[0][1],l1[1][1])
                                    high_val1 = max(l1[0][1],l1[1][1])
                                    low_val2 = min(l2[0][1],l2[1][1])
                                    high_val2 = max(l2[0][1],l2[1][1])
                                    if low_val1 < low_val2 and high_val1 > low_val2:
                                        single_elem = []
                                        single_elem.append(low_val1)
                                        single_elem.append(low_val2)
                                        single_elem.append(high_val1)
                                        single_elem.append(high_val2)
                                        #single_elem = low_val1,low_val2,high_val1,high_val2
                                        single_elem.sort()
                                        vertice_l = l1[0][0],single_elem[1]
                                        intersection.append(vertice_l)
                                        elem = l1[0],l1[1],l2[0],l2[1]
                                        intersection_list[vertice_l].append(elem)
                                        vertice_l = l1[0][0],single_elem[2]
                                        intersection.append(vertice_l)
                                        intersection_list[vertice_l].append(elem)
                                        vertice.append(a1)
                                        vertice.append(b1)
                                        vertice.append(c1)
                                        vertice.append(d1)

                                    elif low_val2 < low_val1 and high_val2 > low_val1:
                                        single_elem = []
                                        single_elem.append(low_val1)
                                        single_elem.append(low_val2)
                                        single_elem.append(high_val1)
                                        single_elem.append(high_val2)
                                        #single_elem = low_val1,low_val2,high_val1,high_val2
                                        single_elem.sort()
                                        vertice_l = l1[0][0],single_elem[1]
                                        intersection.append(vertice_l)
                                        elem = l1[0],l1[1],l2[0],l2[1]
                                        intersection_list[vertice_l].append(elem)
                                        vertice_l = l1[0][0],single_elem[2]
                                        intersection.append(vertice_l)
                                        intersection_list[vertice_l].append(elem)
                                        vertice.append(a1)
                                        vertice.append(b1)
                                        vertice.append(c1)
                                        vertice.append(d1)
                                    else:
                                        sds = 2

                                else:
                                    sds = 2
                            else:
                                y_coordinate1 = l1[0][1] - l1[0][0]*(l1[1][1]-l1[0][1])/(l1[1][0]-l1[0][0])
                                y_coordinate2 = l2[0][1] - l2[0][0]*(l2[1][1]-l2[0][1])/(l2[1][0]-l2[0][0])
                                if y_coordinate1 == y_coordinate2:
                                    low_val1 = min(l1[0][0],l1[1][0])
                                    high_val1 = max(l1[0][0],l1[1][0])
                                    low_val2 = min(l2[0][0],l2[1][0])
                                    high_val2 = max(l2[0][0],l2[1][0])
                                    if low_val1 < low_val2 and high_val1 > low_val2:
                                        single_elem = []
                                        single_elem.append(l1[0])
                                        single_elem.append(l1[1])
                                        single_elem.append(l2[0])
                                        single_elem.append(l2[1])
                                        #single_elem = l1[0],l1[1],l2[0],l2[1]
                                        single_elem.sort(key=takeFirst)
                                        vertice_l = single_elem[1]
                                        elem = l1[0],l1[1],l2[0],l2[1]
                                        intersection.append(vertice_l)
                                        intersection_list[vertice_l].append(elem)
                                        vertice_l = single_elem[2]
                                        intersection.append(vertice_l)
                                        intersection_list[vertice_l].append(elem)
                                        vertice.append(a1)
                                        vertice.append(b1)
                                        vertice.append(c1)
                                        vertice.append(d1)
                                    elif low_val2 < low_val1 and high_val2 > low_val1:
                                        single_elem = []
                                        single_elem.append(l1[0])
                                        single_elem.append(l1[1])
                                        single_elem.append(l2[0])
                                        single_elem.append(l2[1])
                                        single_elem.sort(key=takeFirst)
                                        vertice_l = single_elem[1]
                                        intersection.append(vertice_l)
                                        elem = l1[0],l1[1],l2[0],l2[1]
                                        intersection_list[vertice_l].append(elem)
                                        vertice_l = single_elem[2]
                                        intersection.append(vertice_l)
                                        intersection_list[vertice_l].append(elem)
                                        vertice.append(a1)
                                        vertice.append(b1)
                                        vertice.append(c1)
                                        vertice.append(d1)
                                    else:
                                        sds = 2
                                else:
                                    sds = 2
                        else:
                            sds=2
                        #print("not interesecting")
                    aa=aa+1
                at=at+1


        i=i+1

edge= []

"""

a s1 (1,1) (2,2) (3,3)
a s2 (2,0) (2,9)
a s3 (1,5) (-2,5)
"""
def findinde(kk):
    global vertice

    g=vertice
    x1,y1=kk
    #print vertice, g, x1,y1
    try:
        ab=[g.index(t) for t in g if int(t[0]) == int(x1) and int(t[1])==int(y1)]
        #print ab,ab[0],"Finding index",kk,len(g)
        return ab[0]
    except Exception as e:
        print "Error while finding index",e
        pass

def find_in_intersection(a):
    global intersection
    for w in intersection:
        if w == a:
            return True
    return False


def edges(vertice,intersection):
    global intersection_list
    global edge
    #print "intersection list is ---------------------------------------------"
    #print "intersection=", intersection
    for a in intersection:

        for p in intersection_list[a]:
            inter_list = p


            for w in inter_list:
                temp = []
                temp.append(a)
                l1 = (w,a)
                temp.append(w)
                #print "a=",a, "w=", w
                for kk in vertice:
                    l2 = (kk,a)
                    #print "kk=", kk
                    #print "l1=", l1, "l2=", l2
                    if parallel(l1,l2) == True:
                        #print "here-- adding", kk , "a==", a4
                        #print "parallel"
                        temp.append(kk)
                #print "a---==", temp
                temp_list = list(set(temp))
                if w[0] != a[0]:
                    temp_list.sort(key=takeFirst)
                else:
                    temp_list.sort(key=takeSecond)

                #print "a=", temp_list
                length = len(temp_list)
                i = 1
                first = temp_list[0]
                #print "templist=", temp_list

                while i < length:
                    next_ele = temp_list[i]
                    a1 = findinde(first) + 1
                    a2 = findinde(next_ele) + 1
                    if find_in_intersection(first) or find_in_intersection(next_ele):
                        elem_add = a1,a2
                        edge.append(elem_add)
                    i = i + 1
                    first = next_ele




data_streets =[]
data_street=[]
dat_ = []
while True:
    try:
        input_data =  str(raw_input().lower())
        input_data = re.sub(r"\)\(",") (",input_data)
        #print input_data
        size = len(input_data)
        #print "size=", size
        #print input_data
        i = 0
        name = ""
        while i < size:
            if input_data[i] == '\"':
                #print "here"
                name+=input_data[i]
                i = i + 1
                while input_data[i] != '\"':
                    if input_data[i]!=' ':
                        name+=input_data[i]
                    i = i + 1

            name += input_data[i]
            i = i + 1

        input_data = name
        try:
            data = input_data.split(" ")
        except Exception as e:
            print "No spaces between string"
            print e
        #print input_data,data
        command = data[0]
        temp_list = []
        temp_json={}

        if command == "a":
            hcnt=0
            for hh in input_data:
                if hh =='"':
                    hcnt=hcnt+1
                else:
                    asdsdf=2
            if hcnt !=2:
                raise ValueError('Warning double quotes for street names arent proper')
            else:
                asdas=2






            #print "Start"
            try:
                try:
                    #print "Start1"
                    kk1=0
                    space_count=0

                    for a in input_data:
                        kk1=kk1+1
                        #print input_data
                        #print ord(a)
                        if ord(a)==32:
                            space_count=space_count+1
                        else:
                            asdsa=2
                        if ord(a) ==32 and ord(input_data[kk1])==32 :
                            raise ValueError("Spacing error")


                        else:
                            dummar=2

                    try:
                        if space_count == len(data)-1:
                            asdsa=12
                            #print(space_count,len(data))
                        elif space_count <2:
                            raise ValueError("Incorrect spacing, Quitting program to avoid Locks")

                        else:
                            raise ValueError("incorrect spacing, Quitting to avoid locks")
                    except:
                        pass


                except exception as e:
                    #print e
                    pass

                #print("Data:",data)
                street_name = data[1]
                #print "STREET",street_name, type(street_name)
                i=2
                while i < len(data):
                    try:
                        #print data
                        strs = literal_eval(re.sub('(\))(\s+)(\()','\g<1>,\g<3>',data[i]))
                    except Exception as e:
                        #("Error in string section",data[i])
                        print "Warning check String",e
                        street_name=street_name+" " + data[2]
                        i=i+1
                        try:
                            strs = literal_eval(re.sub('(\))(\s+)(\()','\g<1>,\g<3>',data[i]))
                        except:
                            street_name=street_name+" " + data[3]
                            i=i+1
                            try:
                                strs = literal_eval(re.sub('(\))(\s+)(\()','\g<1>,\g<3>',data[i]))
                            except:
                                street_name=street_name+ " " + data[4]
                                i=i+1
                                pass

                        pass
                    temp_list.append(strs)
                    xx1,yy1=strs
                    try:
                        if type(strs) is tuple:
                            #print "tuple's format is correT",xx1,yy1
                            dummy=2
                            if type(xx1) is int and type(yy1) is int:
                                dummygg=2
                            else:
                                raise ValueError("co-ordinate aren't integer")


                        else:
                            raise ValueError("Some issue in formating of ", strs)
                    except Exception as e :
                        raise ValueError("Error in the street point format",strs,e)
                        pass


                    i=i+1
                data_file = {street_name:temp_list}
                if data_file not in data_streets:
                    data_streets.append(data_file)
                #print data_streets
                    data_point.append(temp_list)
                else:
                    print "Street already exists"
                    pass
                #print(data_point)

            except Exception as e :
                print "error" + repr(e)
                #print("check format of vertices",e)
                pass



        elif command =="r":
            data_st=[]
            #data_file = read_file()
            temp_list=[]
            data_p=[]
            data_street= data_streets
            try:
                street_name = data[1]
                i=2
                fl=0
                #print "DATA",data
                try:
                    while i < len(data):
                        strs = literal_eval(re.sub('(\))(\s+)(\()','\g<1>,\g<3>',data[i]))
                        temp_list.append(strs)
                        i=i+1
                    line_dat=""
                except:
                    pass
                op=2

                aa=0
                for line in data_street:
                    try:
                        datas= line
                        for k,v in datas.iteritems():
                            #print k,v
                            asdsad=2
                            key=k
                            val =v
                        if key == street_name:
                            data_street.pop(aa)
                            #ko=  { street_name:temp_list}
                            #data_street.append(ko)

                        aa=aa+1

                    except Exception as e:
                        #print e
                        pass
                data_point =[]
                for line in data_street:
                    try:
                        datas= line
                        for k,v in datas.iteritems():
                            #print k,v
                            asdsad=2
                            key=k
                            val =v
                        data_point.append(val)
                        #print data_point
                        aa=aa+1

                    except Exception as e:
                        #print e
                        pass
                #print data_point, data_street,"DATA"




            except Exception as e:
                print "error in parsing",e
                pass


        elif command =="c":
            data_st=[]
            #data_file = read_file()
            temp_list=[]
            data_p=[]
            data_street= data_streets
            try:
                street_name = data[1]
                i=2
                fl=0
                #print "DATA",data
                while i < len(data):
                    strs = literal_eval(re.sub('(\))(\s+)(\()','\g<1>,\g<3>',data[i]))
                    temp_list.append(strs)
                    i=i+1
                line_dat=""
                op=2

                aa=0
                for line in data_street:
                    try:
                        datas= line
                        for k,v in datas.iteritems():
                            #print k,v
                            asdsad=2
                            key=k
                            val =v
                        if key == street_name:
                            data_street.pop(aa)
                            ko=  { street_name:temp_list}
                            data_street.append(ko)
                        else:
                            print "Doesn't exist"
                            #print "ok"
                        aa=aa+1

                    except Exception as e:
                        #print e
                        pass
                data_point =[]
                for line in data_street:
                    try:
                        datas= line
                        for k,v in datas.iteritems():
                            #print k,v
                            asdsad=2
                            key=k
                            val =v
                        data_point.append(val)
                        #print data_point
                        aa=aa+1

                    except Exception as e:
                        print e
                        pass
                #print data_point, data_street,"DATA"




            except Exception as e:
                print "error in parsing",e
                pass






        elif command =="g":
            vn=[]
            intersection=[]
            #data_file = read_file()
            check_vert()
            vertice = list(set(vertice))
            intersection = list(set(intersection))

            vertice = list(set(vertice))

            edges(vertice,intersection)
            sd=0
            aa=""
            ed_t=""
            for a in vertice:
                gg="V"+str(sd)
                sd=sd+1
                aa = aa + "\n" + gg + ":   "+ str(a)

            print "V =","{"  + aa +"\n"+"}"
            #print "Edges",list(set(edge))
            print "E = {"
            edge=list(set(edge))
            if len(edge)==0:
                print "}"
            else:
                for j in range(0,len(edge)):
                    a = str(edge[j][0]-1)
                    b = str(edge[j][1]-1)

                    if j != len(edge)-1:
                        ed_t = ed_t + "<"+ a+ ","+ b + ">"+"," +"\n"
                        print "<%s,%s>, "%(a,b)
                    elif j ==  len(edge)-1 or len(edge):
                        print "<%s,%s>"%(a,b),"\n"+"}"

            #print "Edge","{" +"\n" + ed_t +"\n"+"}"
            #for k, v in data_file.items():
             #   v.append(data_points)
            #print vertice
            vertice=[]
            ed_t=[]
            edge=[]
            intersection_list = defaultdict(list)









        else:
            print("Enter a valid commnad i.e a,c,r,q")
    except Exception as e :
        break
        #print("Error in data format",e)
        #pass
