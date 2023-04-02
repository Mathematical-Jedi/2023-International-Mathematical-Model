# library(xlsx)
# df <- read.xlsx('../../data/爬取的数据_cleaned_Price缺失较多-无地区信息.xlsx')
df <- read.csv('yecanming/爬虫数据特征工程/r-data1.csv')

str(df)
summary(df$Price)
hist(df$Price)

table(df$Features.Electronics.Vcr)

# c('Basics.Year',
#  'Basics.Length (ft)',
#  'Propulsion.TotalPower (hp)',
#  'Specifications.Dimensions.LengthOverall (ft)',
#  'Specifications.Dimensions.Beam (ft)',
#  'Specifications.Accommodations.DoubleBerths',
#  'Specifications.Accommodations.Cabins',
#  'Specifications.Accommodations.Heads',
#  'Basics.HullWarranty (years)',
#  'Propulsion.EngineYear',
#  'Propulsion.EngineHours',
#  'Propulsion.PropellerType',
#  'Specifications.Speed&Distance.CruisingSpeed (kn)',
#  'Specifications.Speed&Distance.MaxSpeed (kn)',
#  'Specifications.Dimensions.LengthOnDeck (ft)',
#  'Specifications.Dimensions.MaxDra (ft)',
#  'Specifications.Dimensions.CabinHeadroom (ft)',
#  'Specifications.Dimensions.LengthAtWaterline (ft)',
#  'Specifications.Dimensions.MaxBridgeClearance (ft)',
#  'Specifications.Weights.DryWeight (Lb)',
#  'Specifications.Accommodations.SingleBerths',
#  'Propulsion.FoldingPropeller',
#  'Specifications.Accommodations.TwinBerths',
#  'Specifications.Miscellaneous.ElectricalCircuit (V)',
#
#  'Specifications.Miscellaneous.SeatingCapacity',
#
#  'Specifications.Speed&Distance.Range (nm)',
#  'Specifications.Dimensions.Freeboard (ft)',
#  'Specifications.Miscellaneous.LiferaftCapacity',
#  'Propulsion.RopeCutter',
#  'Specifications.Miscellaneous.DeadriseAtTransom (deg)',
# )
# continu<-c('Price', 'Basics.Year', 'Basics.Length..ft.', 'Propulsion.TotalPower..hp.', 'Specifications.Dimensions.LengthOverall..ft.', 'Specifications.Dimensions.Beam..ft.',  'Propulsion.EngineYear', 'Propulsion.EngineHours', 'Specifications.Speed.Distance.CruisingSpeed..kn.', 'Specifications.Speed.Distance.MaxSpeed..kn.', 'Specifications.Dimensions.LengthOnDeck..ft.', 'Specifications.Dimensions.CabinHeadroom..ft.', 'Specifications.Dimensions.LengthAtWaterline..ft.', 'Specifications.Dimensions.MaxBridgeClearance..ft.', 'Specifications.Weights.DryWeight..Lb.', 'Specifications.Speed.Distance.Range..nm.', 'Specifications.Dimensions.Freeboard..ft.')

continu <- c("Price", "Basics.Length..ft.","Propulsion.TotalPower..hp.","Specifications.Accommodations.DoubleBerths","Specifications.Accommodations.Cabins","Specifications.Accommodations.Heads","Propulsion.EngineYear","Specifications.Speed.Distance.CruisingSpeed..kn.","Specifications.Speed.Distance.MaxSpeed..kn.","Specifications.Dimensions.LengthOnDeck..ft.","Specifications.Dimensions.LengthAtWaterline..ft.","Specifications.Dimensions.MaxBridgeClearance..ft.")
cor(df[continu])

library(psych)

# pairs.panels(df[continu])

df$LogPrice<-log(df$Price)
hist(df$LogPrice)

continu2 <- c("LogPrice", "Basics.Length..ft.","Propulsion.TotalPower..hp.","Specifications.Accommodations.DoubleBerths","Specifications.Accommodations.Cabins","Specifications.Accommodations.Heads","Propulsion.EngineYear","Specifications.Speed.Distance.CruisingSpeed..kn.","Specifications.Speed.Distance.MaxSpeed..kn.","Specifications.Dimensions.LengthOnDeck..ft.","Specifications.Dimensions.LengthAtWaterline..ft.","Specifications.Dimensions.MaxBridgeClearance..ft.")

pairs.panels(df[continu2])

model <- lm (LogPrice~Basics.Length..ft.+Propulsion.TotalPower..hp.+Specifications.Accommodations.DoubleBerths+Specifications.Accommodations.Cabins+Specifications.Accommodations.Heads+Propulsion.EngineYear+Specifications.Speed.Distance.CruisingSpeed..kn.+Specifications.Speed.Distance.MaxSpeed..kn.+Specifications.Dimensions.LengthOnDeck..ft.+Specifications.Dimensions.LengthAtWaterline..ft.+Specifications.Dimensions.MaxBridgeClearance..ft., data = df)
summary(model)
# model <- lm (Price~Basics.Length..ft.+Propulsion.TotalPower..hp.+Specifications.Accommodations.DoubleBerths+Specifications.Accommodations.Cabins+Specifications.Accommodations.Heads+Propulsion.EngineYear+Specifications.Speed.Distance.CruisingSpeed..kn.+Specifications.Speed.Distance.MaxSpeed..kn.+Specifications.Dimensions.LengthOnDeck..ft.+Specifications.Dimensions.LengthAtWaterline..ft.+Specifications.Dimensions.MaxBridgeClearance..ft., data = df)

