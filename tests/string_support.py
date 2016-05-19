import io



def getStringFromSerialyser(serialyser, matches):
    out = io.StringIO
    serialyser.saveMatches(matches, out)
    return out