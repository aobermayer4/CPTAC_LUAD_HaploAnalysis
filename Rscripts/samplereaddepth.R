library(tidyr)
library(ggplot2)
library(dplyr)
library(plotly)

## sample data frame formation
# TCGA big set
tcga5.df <- read.table("~/R/LUADdgeAnalysis/ReadDepthData/TCGA_depthgt5_P.txt", header=T)
tcga10.df <- read.table("~/R/LUADdgeAnalysis/ReadDepthData/TCGA_depthgt10_P.txt", header=T)
# CPTAC sample set
cptac5.df <- read.table("~/R/LUADdgeAnalysis/ReadDepthData/CPTAC_depthgt5_P.tsv", header=T)
cptac10.df <- read.table("~/R/LUADdgeAnalysis/ReadDepthData/CPTAC_depthgt10_P.tsv", header=T)

## create depth fraction vectors
# TCGA
tcga5.dpf <- tcga5.df$DepthFraction
tcga10.dpf <- tcga10.df$DepthFraction
cptac5.dpf <- cptac5.df$DepthFraction
cptac10.dpf <- cptac10.df$DepthFraction

# assigning colors
barfill <- 'cadetblue3'
barlines <- 'cadetblue4'


## interactive point plots of TCGA samples DepthFraction vs MeanDepth

# TCGA >5 read depth
tcga5p <- ggplot(tcga5.df, aes(x=DepthFraction, y=MeanDepth,
                               text = paste('</br> Sample: ', Sample,
                                            '</br> Depth Fraction: ', DepthFraction,
                                            '</br> MeanDepth: ', MeanDepth,
                                            '</br> MedianDepth: ', MedianDepth))) +
  geom_point(color = barlines) +
  labs(x="Fraction of Bases with Read Depth > 5",
       y="Mean Depth of Sample",
       title="TCGA Samples: Fraction of Bases\nRead Depth of 5 or Greater") +
  theme_minimal()
ggplotly(tcga5p, tooltip="text")

# TCGA >10 read depth
tcga10p <- ggplot(tcga10.df, aes(x=DepthFraction, y=MeanDepth,
                      text = paste('</br> Sample: ', Sample,
                                   '</br> Depth Fraction: ', DepthFraction,
                                   '</br> MeanDepth: ', MeanDepth,
                                   '</br> MedianDepth: ', MedianDepth))) +
  geom_point(color = barlines) +
  labs(x="Fraction of Read Depth Greater than 10",
       y="Mean Depth of Sample",
       title="TCGA Samples with Depth Coverage of 10 or Greater") +
  theme_minimal()
ggplotly(tcga10p, tooltip="text")


# histogram of TCGA5 all
ggplot(tcga5.df, aes(x = tcga5.dpf)) +
  geom_histogram(color = barlines,
                 fill = barfill,
                 bins = 35) +
  scale_x_continuous(name = "Fraction of Reads with Depth > 5",
                     breaks = seq(0,1,0.1),
                     limits = c(0,1)) +
  ggtitle("Read Depth Fraction Frequency: >5") +
  scale_y_continuous(name = "Samples",
                     seq(0,35,5),
                     limits = c(0,35)) +
  theme_minimal()

# histogram of TCGA10 all
ggplot(tcga10.df, aes(x = tcga10.dpf)) +
  geom_histogram(color = barlines,
                 fill = barfill,
                 bins = 35) +
  scale_x_continuous(name = "Fraction of Reads with Depth > 10",
                     breaks = seq(0,1,0.1),
                     limits = c(0,1)) +
  ggtitle("TCGA Fraction Read Depth > 10") +
  scale_y_continuous(name = "Samples",
                     seq(0,15,5),
                     limits = c(0,15)) +
  theme_minimal()

# Bar Plots

TCGAbar <- ggplot(tcga5.df, aes(x=reorder(Sample, MeanDepth), y=MeanDepth,
                     text = paste('</br> Sample: ', Sample,
                                  '</br> Depth Fraction: ', DepthFraction,
                                  '</br> MeanDepth: ', MeanDepth,
                                  '</br> MedianDepth: ', MedianDepth))) +
  geom_bar(stat = "identity",
           color = barlines,
           fill = barfill,
           position = "dodge") +
  theme_minimal() +
  ggtitle("Mean Read Depth per Sample: TCGA") +
  xlab("Sample") +
  scale_y_continuous(name = "Mean Depth",
                     seq(0,200,50),
                     limits = c(0,200),
                     label = scales::comma) +
  theme(axis.text.x = element_blank())
ggplotly(TCGAbar, tooltip="text")

#CPTAC Read Depth bar plot
CPTACbar <- ggplot(cptac5.df, aes(x=reorder(Sample, MeanDepth), y=MeanDepth,
                       text = paste('</br> Sample: ', Sample,
                                    '</br> Depth Fraction: ', DepthFraction,
                                    '</br> MeanDepth: ', MeanDepth,
                                    '</br> MedianDepth: ', MedianDepth))) +
  geom_bar(stat = "identity",
           color = barlines,
           fill = barfill,
           position = "dodge") +
  theme_minimal() +
  theme(axis.text.x = element_blank()) +
  ggtitle("Mean Read Depth per Sample: CPTAC") +
  xlab("Sample") +
  scale_y_continuous(name = "Mean Depth",
                     seq(0,900,100),
                     limits = c(0,900),
                     label = scales::comma)
ggplotly(CPTACbar, tooltip="text")

