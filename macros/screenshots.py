for (name, i), l in GetLayouts().items():
    print name
    print i
    print l
    for iv, v in enumerated(GetViewsInLayout(l)):
        print v
        SaveScreenshot('c:/my/work/"{}"/{}.png'.format(name, iv), v)

 