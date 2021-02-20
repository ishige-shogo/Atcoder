#提出の基本となる部分
# 整数の入力
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

b = data.to_s(2)

Integer("0377"


#-----------------------------------------------------------
#ミスったーーーー！
X = gets.to_i
M = gets.to_i

s = X.to_s.split(//).max.to_i + 1

r = X.to_s.split(//).reverse.to_i

ans = 0
count=0

while true do
    break if s>16
    ans = X.to_s(s).to_i
    s += 1
    break if ans > M
    count += 1
end

puts count



#----------------------------------------------------------------
N,K = gets.chomp.split(" ").map(&:to_i);

def kaprekar(m)
    s = m.to_s
    s_big = s.split(//).sort.reverse.join.to_i
    s_small = s.split(//).sort.join.to_i
    return s_big - s_small
end

count = 1
while count<=K do
    N = kaprekar(N)
    count += 1
end

puts N
#--------------------------------------------------
S = gets.chomp.split(//)
def up(n)
    [*"A".."Z"].include?(n)
end

def down(w)
    [*"a".."z"].include?(w)
end

count = 0
S.each_with_index do |s,i|
    if ((i+1).odd? && down(s)) || ((i+1).even? && up(s))
        count +=1
    end
end

if count==S.length
    puts "Yes"
else
    puts "No"
end



#-----------------------------------------------
X = gets.to_i

y = X/100

puts (y+1)*100-X