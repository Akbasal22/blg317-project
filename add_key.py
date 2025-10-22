import pandas as pd

# df = pd.read_csv("./datas/transfers.csv")
# df['transfer_id'] = df.index + 1
# df.insert(loc=0, column="transfer_id", value=df.pop('transfer_id'))
# df.to_csv(index=False, path_or_buf="./datas/transfers1.csv")


# df = pd.read_csv("./datas/player_valuations.csv")
# # df['valuation_id'] = df.index + 1
# df = df.drop(columns=['transfer_id'])
# # df.insert(loc=0, column="valuation_id", value=df.pop('valuation_id'))
# df.to_csv(index=False, path_or_buf="./datas/player_valuations.csv")

df = pd.read_csv("./datas/club_games.csv")
df['game_id'] = (df['game_id'].astype(str) + (df['hosting'] == 'Home').astype(int).astype(str)).astype(int)
df.to_csv(index=False, path_or_buf="./datas/club_games1.csv")