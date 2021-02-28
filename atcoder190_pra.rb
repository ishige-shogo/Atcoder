#5分
A,B,C=gets.chomp.split(" ").map(&:to_i);
if A > B || (A == B && C == 1)
    puts Takahashi
else
    puts Aoki
end

#---------------------------------------------------------
#20分
N,S,D=gets.chomp.split(" ").map(&:to_i);

magic = Array.new(N)

N.times do |n|
    x, y = gets.chomp.split(" ").map(&:to_i);
    magic[n] = [x, y]
end

#カウントを0と置く
count = 0
0.upto(N-1) do |n|
    #詠唱時間が規定より小さい且つダメージが規定より大きい場合、カウントを足して処理を終了
    if ((magic[n][0] < S) && (magic[n][1] > D))
        count += 1
        break
    end
end

#カウントが
if count==0
    puts "No"
else
    puts "Yes"
end

#------------------------------------------------------

N, M = gets.chomp.split(" ").map(&:to_i);

conditions = Array.new()

M.times do |m|
    a, b = gets.chomp.split(" ").map(&:to_i);
    conditions[m] = [a, b]
end

K = gets.to_i

people = Array.new()

K.times do |k|
    c, d = gets.chomp.split(" ").map(&:to_i);
    people[k] = [c, d]
end

bit = Array.new()

bit_line = [*0...(K**2)]

bit_line.each do |b|
    bit.append([b.to_s(2).split(//)])
end

ary = Array.new()


bit.each do |b|
    K.times do |k|
        while true do
            
        end
    end
end


