
libary('ggplot2')

df<-read.csv('Bar.csv',header = TRUE,sep = ',')
df
bar_chart<-ggplot(df,aes(Brand,Cars.Listings))+
                  geom_bar(stat='identity',color='darkblue',fill='darkblue',width = 0.8)+
                  theme_light()+
                  ggtitle('Cars Listings by Brand')+
                  labs(x=NULL,y='Number of Cars Listings',size=13)+
                  theme(axis.text.x = element_text(angle = 45,hjust=1,size = 13))+
                  theme(axis.text.y = element_text(size = 13))
  
bar_chart

