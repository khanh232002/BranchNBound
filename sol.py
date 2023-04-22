#Đọc file lấy dữ liệu
with open('input.txt') as f:
    m, n = [int(x) for x in next(f).split()]
    W = [int(x) for x in next(f).split()]
    V = [int(x) for x in next(f).split()]

#Code chính
def BnB(i):
    #Lấy global, tui cũng ko biết cách nào ngon hơn :(
    global S,W_cur,x,Best,Best_sol

    #Tính số lần chọn đá tốt hạng i
    t = int((m-W_cur)/W[i])

    #j lặp số lần từ t xuống 0
    for j in range(0,t+1):

        #Thêm j viên đá tốt hạng i vào, update tổng giá trị và trọng lượng
        x[i] = j
        W_cur += W[i]*x[i]
        S += V[i]*x[i]

        #Xét đã đạt lời giải
        if (i == n-1):
            if (S > Best):
                #Update Best
                Best_sol[:] = x[:]
                Best = S

        else:
            #Tính cận bằng cách nhét đầy khoảng trống còn lại bằng viên đá tốt tiếp theo (i+1)
            g = S + int(V[i+1]*(m-W_cur)/W[i+1])

            #Kiểm tra bound, tốt hơn Best thì chọn viên đá tiếp theo
            if (g>Best):
                BnB(i+1)

        #Trả giá trị lại về trước đó
        W_cur -= W[i]*x[i]
        S -= V[i]*x[i]

#Khởi tạo các giá trị
S = int(0)
W_cur = int(0)
x = [0] * n
Best = int(0)
Best_sol = [0] * n

#Sắp xếp giá trị theo tỉ lệ (Giá trị)/(Trọng lượng)
order = [i for i in range(len(W))] #lưu lại thứ tự gốc
VW = zip(V, W, order) 
VW = sorted(VW, key=lambda t: t[0]/t[1], reverse=True) 
print(VW)
V, W, order = zip(*VW)

#Triển
BnB(0)

#Sắp xếp lại
VW = zip(Best_sol, order) 
VW = sorted(VW, key=lambda t: t[1]) 
Best_sol, order = zip(*VW)

#Xuất
with open(r'output.txt', 'w') as fp:
    for i in Best_sol:
        fp.write("%s " % i)    
    fp.write("\n%s" % Best)
                
            
                
