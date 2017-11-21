for v in GetRenderViews():
    if v.InteractionMode == '2D':
        v.UseLight = False
        v.LightSwitch = 1