X = gets.chomp
M = gets.to_i

#Xの逆順番
x_lines = X.split(//).reverse

#文字列X中の最大の数字: d
x_max = X.split(//).max.to_i

ans = 0

n = x_max + 1

while true do
    sum = 0
    x_lines.each_with_index do |x, i|
        sum += x.to_i * (n ** i)
    end
    sum <= M ? ans += 1 : break
    n += 1
end

puts ans

data = (0..50000000)
puts data.bsearch {|number| number > 40000000 }


data = (0..50000000)
puts data.find {|number| number > 40000000 }