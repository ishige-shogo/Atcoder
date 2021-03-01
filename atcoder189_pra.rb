#4分(A問題)
a,b,c=gets.chomp.split(//)

if a==b && b==c && a==c
    puts "Won"
else
    puts "Lost"
end

#-------------------------------------------------

N,X=gets.chomp.split(" ").map(&:to_i);

beer = Array.new(N){gets.split.map(&:to_i)}

amount = 0
count = 0

beer.each do |b|
    amount += b[0] * b[1] / 100.to_f
    count += 1
    if amount > X
        puts count
        break
    end
end

if amount <= X
    puts -1
end

#--------------------------------------------------