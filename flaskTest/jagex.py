from OSRS_Hiscores import Hiscores
from flask_table import Table,Col


'''
def fixformat(ign):
    ign.replace(' ', '_')
    user = Hiscores(str(ign), 'N')
    return user
    return user.stats['attack']['level']
'''
'''
def SkillResults(ign):
    skills = ('attack', 'strength', 'defense', 'ranged', 'prayer', 'magic', 'runecrafting', 'construction', 'hitpoints',
          'agility', 'herblore', 'thieving', 'crafting', 'fletching', 'slayer', 'hunter', 'mining', 'smithing', 'fishing',
          'cooking', 'firemaking', 'woodcutting', 'farming')
    skilllist = []
    stringingamename=str(ign)
    spacelessIGN=stringingamename.replace(" ", "_")
    user = Hiscores(spacelessIGN.lower(), 'N')
    for i in range(len(skills)):
        skilllist.append(str('Your ' + str(skills[i] + " level is " + str(user.stats[skills[i]]['level']))))
    return skilllist
'''
class levelTable(Table):
    NameSkill = Col('Skill Name')
    LevelSkill = Col('Level')

def CommaNumber(numb):
    return (f"{numb:,}")

def XpForLevel(level):
    return round((1/4)*((1/2)*level**2-(1/2)*level+300*2**(1/7)*((2**((level-1)/7)-1)/(2**(1/7)-1))))

def SkillResults(ign):
    skills = ('Attack', 'Strength', 'Defense', 'Ranged', 'Prayer', 'Magic', 'Runecrafting', 'Construction', 'Hitpoints',
          'Agility', 'Herblore', 'Thieving', 'Crafting', 'Fletching', 'Slayer', 'Hunter', 'Mining', 'Smithing', 'Fishing',
          'Cooking', 'Firemaking', 'Woodcutting', 'Farming')
    try:
        skilllist = []
        skilldictionary = dict()
        skillnamedictionary = dict()
        stringingamename=str(ign)
        spacelessIGN=stringingamename.replace(" ", "_")
        user = Hiscores(spacelessIGN.lower(), 'N')
        for i in range(len(skills)):
            skilldictionary[str(skills[i])] = str(user.stats[skills[i].lower()]['level'])
        return skilldictionary
    except:
        skilldictionary['ERROR!'] = str('The lookup attempt was successful but no results were returned. Make sure your spelling is correct and OSRS is not down!')
        return skilldictionary


#Gets the XP remaining until this level
#POSSIBLE USE CASE: if playerstat less than achievementdiarylevelrequirements, return XpLeft 
def allXpLeft(ign):
    skills = ('Attack', 'Strength', 'Defense', 'Ranged', 'Prayer', 'Magic', 'Runecrafting', 'Construction', 'Hitpoints',
          'Agility', 'Herblore', 'Thieving', 'Crafting', 'Fletching', 'Slayer', 'Hunter', 'Mining', 'Smithing', 'Fishing',
          'Cooking', 'Firemaking', 'Woodcutting', 'Farming')
    
    AchievementDiaryLevelRequirements = {
    'attack' : 50,    'strength' : 76,    'defense' : 70,    'ranged' : 70,    'prayer' : 85,    'magic' : 96,    'runecrafting' : 91,    'construction' : 78,    'hitpoints' : 70,
    'agility' : 90,    'herblore' : 90,    'thieving' : 91,    'crafting' : 85,    'fletching' : 95,    'slayer' : 95,    'hunter' : 70,    'mining' : 85,    'smithing' : 91,
    'fishing' : 96,    'cooking' : 95,    'firemaking' : 85,    'woodcutting' : 90,    'farming' : 91,
    }
    
    AchievementDiaryXpMissing = dict()

    try:
        stringingamename=str(ign)
        spacelessIGN=stringingamename.replace(" ", "_")
        user = Hiscores(spacelessIGN.lower(), 'N')    
        
        for i in range(len(skills)):
            XpTarget = XpForLevel(AchievementDiaryLevelRequirements[str(skills[i].lower())])
            XpNow = user.stats[skills[i].lower()]['experience']
            XpRemainder = XpTarget - XpNow
            if XpRemainder > 0:
                AchievementDiaryXpMissing[str(skills[i])] = CommaNumber(XpRemainder)
        return AchievementDiaryXpMissing
    except:
        AchievementDiaryXpMissing['ERROR!'] = 'Check above for details'
        return AchievementDiaryXpMissing

def allXpLeftQUEST(ign):
    skills = ('Attack', 'Strength', 'Defense', 'Ranged', 'Prayer', 'Magic', 'Runecrafting', 'Construction', 'Hitpoints',
          'Agility', 'Herblore', 'Thieving', 'Crafting', 'Fletching', 'Slayer', 'Hunter', 'Mining', 'Smithing', 'Fishing',
          'Cooking', 'Firemaking', 'Woodcutting', 'Farming')
    
    QuestCapeLevelRequirements = {
    'attack' : 50,    'strength' : 50,    'defense' : 65,    'ranged' : 60,    'prayer' : 50,    'magic' : 75,    'runecrafting' : 55,    'construction' : 70,
    'hitpoints' : 50,    'agility' : 70,    'herblore' : 70,    'thieving' : 60,    'crafting' : 70,    'fletching' : 60,    'slayer' : 69,    'hunter' : 70,
    'mining' : 72,    'smithing' : 70,    'fishing' : 62,    'cooking' : 70,    'firemaking' : 66,    'woodcutting' : 71,    'farming' : 70,
    }
    
    QuestCapeXpMissing = dict()

    try:
        stringingamename=str(ign)
        spacelessIGN=stringingamename.replace(" ", "_")
        user = Hiscores(spacelessIGN.lower(), 'N')    
        
        for i in range(len(skills)):
            XpTarget = XpForLevel(QuestCapeLevelRequirements[str(skills[i].lower())])
            XpNow = user.stats[skills[i].lower()]['experience']
            XpRemainder = XpTarget - XpNow
            if XpRemainder > 0:
                QuestCapeXpMissing[str(skills[i])] = CommaNumber(XpRemainder)
        return QuestCapeXpMissing
    except:
        QuestCapeXpMissing['ERROR!'] = 'Check above for details'
        return QuestCapeXpMissing
    
def allXpLeftMAX(ign):
    skills = ('Attack', 'Strength', 'Defense', 'Ranged', 'Prayer', 'Magic', 'Runecrafting', 'Construction', 'Hitpoints',
          'Agility', 'Herblore', 'Thieving', 'Crafting', 'Fletching', 'Slayer', 'Hunter', 'Mining', 'Smithing', 'Fishing',
          'Cooking', 'Firemaking', 'Woodcutting', 'Farming')
    
    MaxCapeXpMissing = dict()

    try:
        stringingamename=str(ign)
        spacelessIGN=stringingamename.replace(" ", "_")
        user = Hiscores(spacelessIGN.lower(), 'N')    
        
        for i in range(len(skills)):
            XpTarget = 13034431 
            XpNow = user.stats[skills[i].lower()]['experience']
            XpRemainder = XpTarget - XpNow
            if XpRemainder > 0:
                MaxCapeXpMissing[str(skills[i])] = CommaNumber(XpRemainder)
        return MaxCapeXpMissing
    except:
        MaxCapeXpMissing['ERROR!'] = 'Check above for details'
        return MaxCapeXpMissing


## BIG CHUNK INCOMING PRE TESTING ###


agilityBoost = {
    'Elven dawn': 1,
    'Agility potion': 3,
    'Agility mix': 3,
    'Summer pie': 5,
    'Spicy stew': 5,
}

attackBoost = {
    'Blood pint': 5,
    'Spicy stew': 5,
}

constructionBoost ={
    'Cup of tea': 3,
    'Spicy stew': 5,
}

cookingBoost = {
    "Spicy stew": 5,
    "Chef's delight (m)": 6,
}

craftingBoost = {
    'Mushroom pie': 4,
    'Spicy stew': 5,
}

defenseBoost = {
    'Excalibur': 8,
    'Spicy stew': 5,
}

farmingBoost = {
    'Garden pie': 3,
    'Spicy stew': 5,
}

firemakingBoost = {
    'Spicy stew': 5,
}

fishingBoost = {
    'Fish pie': 3,
    'FIshing potion': 3,
    'Dragon harpoon': 3,
    'Admiral pie': 5,
    'Spicy stew': 5,
}

fletchingBoost = {
    'Dragonfruit pie': 4,
    'Spicy stew': 5,
}

herbloreBoost = {
    "Greenman's ale": 1,
    "Mature Greenman's ale": 2,
    'Botanical pie': 4,
    'Spicy stew': 5,
}

hitpointsBoost = {
    'Bloody bracer': 2,
    'Guthix rest': 5,
    'Amulet of the damned': 10,
}

hunterBoost = {
    'Hunter potion': 3,
    'Spicy stew': 5,
}

magicBoost = {
    'Magic potion': 4,
    'Spicy stew': 5,
    'Imbued heart': 9,
}

miningBoost = {
    'Dwarven stout': 1,
    'Dwarven stout (m)': 2,
    'Dragon pickaxe': 3,
    'Spicy stew': 5,
}

prayerBoost = {
    'Spicy stew': 5,
    'God wars dungeon altar': 11,
}

rangedBoost = {
    'Wild pie': 4,
    'Lizardkicker': 4,
    'Spicy stew': 5,
}

runecraftingBoost = {
    'Oldak': 2,
    'Spicy stew': 5,
}

slayerBoost = {
    "Slayer's respite": 2,
    "Mature slayer's respite": 4,
    'Wild pie': 5,
    'Spicy stew': 5,
}

smithingBoost = {
    'Dwarven stout': 1,
    'Dwarven stout (m)': 2,
    'Spicy stew': 5,
}

strengthBoost = {
    'Jangerberries': 1,
    "Braindeath 'rum'": 3,
    'Blood pint': 5,
    "Spicy stew": 5,
}

thievingBoost = {
    "Spring sq'irkjuice": 1,
    "Autumn sq'irkjuice": 2,
    "Summer sq'irkjuice": 3,
    'Spicy stew': 5,
}

woodcuttingBoost = {
    "Axeman's folly": 1,
    "Mature axeman's folly": 2,
    'Dragon axe': 3,
    'Spicy stew': 5,
}

nestedBoostDict = (attackBoost, strengthBoost, defenseBoost, rangedBoost, prayerBoost, magicBoost, runecraftingBoost, constructionBoost, hitpointsBoost, agilityBoost,
          herbloreBoost, thievingBoost, craftingBoost, fletchingBoost, slayerBoost, hunterBoost, miningBoost, smithingBoost, fishingBoost, cookingBoost, firemakingBoost, 
          woodcuttingBoost, farmingBoost)


def WITHBOOSTSallXpLeft(ign):
    skills = ('Attack', 'Strength', 'Defense', 'Ranged', 'Prayer', 'Magic', 'Runecrafting', 'Construction', 'Hitpoints',
          'Agility', 'Herblore', 'Thieving', 'Crafting', 'Fletching', 'Slayer', 'Hunter', 'Mining', 'Smithing', 'Fishing',
          'Cooking', 'Firemaking', 'Woodcutting', 'Farming')

    AchievementDiaryLevelRequirements = {
    'attack' : 50,    'strength' : 76,    'defense' : 70,    'ranged' : 70,    'prayer' : 85,    'magic' : 96,    'runecrafting' : 91,    'construction' : 78,    'hitpoints' : 70,
    'agility' : 90,    'herblore' : 90,    'thieving' : 91,    'crafting' : 85,    'fletching' : 95,    'slayer' : 95,    'hunter' : 70,    'mining' : 85,    'smithing' : 91,
    'fishing' : 96,    'cooking' : 95,    'firemaking' : 85,    'woodcutting' : 90,    'farming' : 91,
    }
    
    BoostAchievementDiaryXpMissing = dict()


    try:
        stringingamename=str(ign)
        spacelessIGN=stringingamename.replace(" ", "_")
        user = Hiscores(spacelessIGN.lower(), 'N')    
        
        for i in range(len(skills)):
            XpTarget = XpForLevel(AchievementDiaryLevelRequirements[str(skills[i].lower())])
            XpNow = user.stats[skills[i].lower()]['experience']
            XpRemainder = XpTarget - XpNow
            if XpRemainder > 0:
                BoostAchievementDiaryXpMissing[str(skills[i])] = CommaNumber(XpRemainder)
                for j in range(len(nestedBoostDict)):
                    for key, value in nestedBoostDict[i].items():
                        if user.stats[skills[i].lower()]['level'] + value >= AchievementDiaryLevelRequirements[str(skills[i].lower())]:
                            BoostAchievementDiaryXpMissing[str(skills[i])] = ('You may boost using ' + str(key) + ' or better.')
                            break
            else:
                BoostAchievementDiaryXpMissing[str(skills[i])] = ('You can complete the diaries without boosting this skill.')
        return BoostAchievementDiaryXpMissing
    except:
        BoostAchievementDiaryXpMissing['ERROR!'] = 'Check above for details'
        return BoostAchievementDiaryXpMissing

# NEED TO FIND A WAY TO ISOLATE THE BIGGEST BOOST (IE THE LAST DICTIONARY ENTRY. SUBTRACT THE ACHIEVEMNT DIARY LEVEL FROM THIS LEVEL
# AND THEN, USE XPFORLEVEL FORMULA TO CLACULATE REMAINING XP WITH BOOSTS ENABLED. CHECK JUPYTER NOTEBOOK UNTITLED in Python n48 laboratories for notes...








'''
def SkillResults(ign):
    skills = ('Attack', 'Strength', 'Defense', 'Ranged', 'Prayer', 'Magic', 'Runecrafting', 'Construction', 'Hitpoints',
          'Agility', 'Herblore', 'Thieving', 'Crafting', 'Fletching', 'Slayer', 'Hunter', 'Mining', 'Smithing', 'Fishing',
          'Cooking', 'Firemaking', 'Woodcutting', 'Farming')
    try:
        skilllist = []
        skilldictionary = dict()
        skillnamedictionary = dict()
        stringingamename=str(ign)
        spacelessIGN=stringingamename.replace(" ", "_")
        user = Hiscores(spacelessIGN.lower(), 'N')
        for i in range(len(skills)):
            skilldictionary[str(skills[i])] = str(user.stats[skills[i].lower()]['level'])
        return skilldictionary
    except:
        skilldictionary['ERROR!'] = str('The lookup attempt was successful but no results were returned. Make sure your spelling is correct and OSRS is not down!')
        return skilldictionary








def SkillResults(ign):
    skills = ('Attack', 'Strength', 'Defense', 'Ranged', 'Prayer', 'Magic', 'Runecrafting', 'Construction', 'Hitpoints',
          'Agility', 'Herblore', 'Thieving', 'Crafting', 'Fletching', 'Slayer', 'Hunter', 'Mining', 'Smithing', 'Fishing',
          'Cooking', 'Firemaking', 'Woodcutting', 'Farming')
    skilllist = []
    skilldictionary = dict()
    skillnamedictionary = dict()
    stringingamename=str(ign)
    spacelessIGN=stringingamename.replace(" ", "_")
    user = Hiscores(spacelessIGN.lower(), 'N')
    for i in range(len(skills)):
        skilldictionary[str(skills[i])] = str(user.stats[skills[i].lower()]['level'])
    return skilldictionary



def returnSkillNameDictionary():
    skills = ('attack', 'strength', 'defense', 'ranged', 'prayer', 'magic', 'runecrafting', 'construction', 'hitpoints',
          'agility', 'herblore', 'thieving', 'crafting', 'fletching', 'slayer', 'hunter', 'mining', 'smithing', 'fishing',
          'cooking', 'firemaking', 'woodcutting', 'farming')
    skillnamedictionary=dict()
    for i in range(len(skills)):
        skillnamedictionary[i] = str(skills[i])
    return skillnamedictionary
'''


