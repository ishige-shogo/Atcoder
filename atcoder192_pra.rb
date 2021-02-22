
X = gets.chomp
M = gets.to_i

x_max = X.to_s.split(//).max.to_i
x_size = X.to_s.split(//).size


def base_sum(n, str)
    x_line = str.to_s.split(//).reverse

    sum = 0
    x_line.each_with_index do |x, i|
        sum += x.to_i * (n ** i)
    end
    sum
end

n_range = ((x_max + 1)..10**100)
sum_line = n_range.bsearch{|r| base_sum(r, X) > M}.to_i

if x_size == 1
    if X.to_i > M
        puts 0
    else
        puts 1
    end
else
    puts sum_line - (x_max+1)
end



#------------------------------------------------------------
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
