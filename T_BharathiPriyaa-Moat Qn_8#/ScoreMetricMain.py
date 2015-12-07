__author__ = 'bharathipriyaa'
import Metrics

total_df, coke_df, pepsi_df = Metrics.readFiles()
Metrics.calculate_viewability(total_df, coke_df, pepsi_df)
total_df, coke_df, pepsi_df=Metrics.calculateAdStickiness(total_df, coke_df, pepsi_df)
Metrics.calculateCPM(total_df, coke_df, pepsi_df)
