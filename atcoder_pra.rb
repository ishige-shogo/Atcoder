#提出の基本となる部分
a# 整数の入力
a = gets.to_i
# スペース区切りの整数の入力
b,c=gets.chomp.split(" ").map(&:to_i);
# 文字列の入力
s = gets.chomp
# 出力
print("#{a+b+c} #{s}\n")

# a1,a2,a3...anの入力
a = gets.chomp.split(" ").map(&:to_i)
# 列の入力
arr=h.times.map{gets.chomp.split("")}

puts a.reject{|i| i == X}.join(" ")
#入力したものを加工
X,Y,R=gets.chomp.split(" ").map{|i| (i.to_f * 10000).round}


#----------------------------------------------------

N,X=gets.chomp.split(" ").map(&:to_i);
a=gets.chomp.split(" ").map(&:to_i)

puts a.select{|n| n != X}.join(" ")

#-------------------------------------------------


H,W=gets.chomp.split(" ").map(&:to_i);
arr=H.times.map{gets.chomp.split("")}

ans = 0

1.upto(H-1) do |i|
    1.upto(W-1) do |j|
        count = 0
        count +=1 if arr[i][j]=="#"
        count +=1 if arr[i-1][j-1]=="#"
        count +=1 if arr[i][j-1]=="#"
        count +=1 if arr[i-1][j]=="#"
        ans += 1 if (count==1) || (count==3)
    end
end

puts ans

#-------------------------------------------------------

X,Y,R=gets.split(" ").map{|i| (i.to_f * 10000).round}

count = 0
(X-R).upto(X+R+1) do |i|
    (Y-R).upto(Y+R+1) do |j|
        if (((i-X).abs ** 2) + ((j-Y).abs ** 2)) <= R ** 2
            count += 1
        end
    end
end

puts count

ary = [0, 4, 7, 10, 100]

puts (0...ary.size).bsearch {|i| ary[i] >= 6 } 

