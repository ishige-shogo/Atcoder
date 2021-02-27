A,B=gets.chomp.split(" ").map(&:to_i);

A, B =100, 80
puts (((A-B).to_f/A.to_f)*100)

#---------------------------------------------------


a = gets.chomp.split(" ").map(&:to_i)
# 列の入力
arr=h.times.map{gets.chomp.split("")}

N = gets.to_i
g = Array.new(N)
N.times do |n|
  a, p, x = gets.split.map &:to_i
  g[n] = [a, p, x]
end

cost=10**9+1

0.upto(N-1) do |n|
    if (g[n][0] < g[n][2]) && (cost > g[n][1])
        cost = g[n][1]
    end
end

if cost == 10**9+1
    puts -1
else
    puts cost
end

#----------------------------------------------------------------

p (8**(1/2.to_f)).floor



N = gets.to_i

max_n = (N**(1/2.to_f)).floor

number = []

2.upto(max_n) do |i|
    s = 2
    while true do
        break if i**s > N
        number.append(i**s)
        s += 1
    end
end

m = number.uniq.size

puts N-m

#------------------------------------------------------------

