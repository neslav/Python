#
#
#
#
# a = input('ведитеслово')
# start=int(input(6))
# end=int(input(2))

# pyta = input(input('please input'))
# start = int(input('start'))
# end = int(input('end'))
# substring = ''
# i = min(start,end)
# while i <= max(start,end):
#     if i < len(a):
#         substring = substring + a[i]
#     i = i + 1
# print (substring)



# L=700
# v_up = 50
# v_down = 70
# t = 120
# t_ost = t % (L/v_up+L/v_down)
# t_up = L/v_up
# if t_ost < t_up:
# res = t_ost*v_up
# else:
# path = (t_ost - t_up)*v_down
# res = L - path
# print (res)
#
# sequence

# sli = slice(2, 1500, )
# # print(sli)
#
# N=10
# data=true
# while data

# profits = [-12, 20, 2098, 12, -2222]
#
# # найти минимальное неотрицательное есмли нет то 0
#
# min_item = None
#
# # for item = None
#
# for item in profits:
#     if item > 0 and (min_item is None or item < min_item)
#         min_item = item
#
# if min_item is None:
#     min_item = 0
#
# Print (min_item)

popils = ['oleg', 'ira', 'igor', 'Anna']

couples = []

i = 0
for person in popils:
    if i % 2 == 0:
        couples.append([popils[i], popils[i+1]])
    i = i + 1

print(couples)