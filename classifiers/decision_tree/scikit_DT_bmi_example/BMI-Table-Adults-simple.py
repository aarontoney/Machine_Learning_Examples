#--------------------------------------------------------------------------------
# BMI Table if you are over 35 is availabe fromt he NIH. 
# (www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmi_tbl.htm)
#--------------------------------------------------------------------------------
#
# Given BMI table
#
#        BMI | 19 20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35
#        ----+-------------------------------------------------------------------+
# HEIGHT  58 | 91 96 100 105 110 115 119 124 129 134 138 143 148 153 158 162 167 |
# (in in) 59 | 94 99 104 109 114 119 124 128 133 138 143 148 153 158 163 168 173 |
#         60 | 97 10 107 112 118 123 128 133 138 143 148 153 158 163 168 174 179 |
#         61 | 10 10 111 116 122 127 132 137 143 148 153 158 164 169 174 180 185 |
#         62 | 10 10 115 120 126 131 136 142 147 153 158 164 169 175 180 186 191 |
#         63 | 10 11 118 124 130 135 141 146 152 158 163 169 175 180 186 191 197 |
#         64 | 11 11 122 128 134 140 145 151 157 163 169 174 180 186 192 197 204 |
#         65 | 11 12 126 132 138 144 150 156 162 168 174 180 186 192 198 204 210 |
#         66 | 11 12 130 136 142 148 155 161 167 173 179 186 192 198 204 210 216 |
#         67 | 12 12 134 140 146 153 159 166 172 178 185 191 198 204 211 217 223 |
#         68 | 12 13 138 144 151 158 164 171 177 184 190 197 203 210 216 223 230 |
#         69 | 12 13 142 149 155 162 169 176 182 189 196 203 209 216 223 230 236 |
#         70 | 13 13 146 153 160 167 174 181 188 195 202 209 216 222 229 236 243 |
#         71 | 13 14 150 157 165 172 179 186 193 200 208 215 222 229 236 243 250 |
#         72 | 14 14 154 162 169 177 184 191 199 206 213 221 228 235 242 250 258 |
#         73 | 14 15 159 166 174 182 189 197 204 212 219 227 235 242 250 257 265 |
#         74 | 14 15 163 171 179 186 194 202 210 218 225 233 241 249 256 264 272 |
#         75 | 15 16 168 176 184 192 200 208 216 224 232 240 248 256 264 272 279 |
#         76 | 15 16 172 180 189 197 205 213 221 230 238 246 254 263 271 279 287 |
#        ----+-------------------------------------------------------------------+
#                 OBESE_ (>30), Overweight_ (25-30), Normal_ (18.5-25), 
#
#  Underweight is a BMI of less that 18.5, but not tracking that state in this 
#  example.
#
#--------------------------------------------------------------------------------
 
from sklearn import tree

Height_in_Weight_lbs_samples = [[91,58],[96,58],[100,58],[105,58],[110,58],[115,58],[119,58],[124,58],[129,58],[134,58],[138,58],[143,58],[148,58],[153,58],[158,58],[162,58],[167,58], [97,60],[10,60],[107,60],[112,60],[118,60],[123,60],[128,60],[133,60],[138,60],[143,60],[148,60],[153,60],[158,60],[163,60],[168,60],[174,60],[179,60], [10,61],[10,61],[111,61],[116,61],[122,61],[127,61],[132,61],[137,61],[143,61],[148,61],[153,61],[158,61],[164,61],[169,61],[174,61],[180,61],[185,61], [10,62],[10,62],[115,62],[120,62],[126,62],[131,62],[136,62],[142,62],[147,62],[153,62],[158,62],[164,62],[169,62],[175,62],[180,62],[186,62],[191,62], [10,63],[11,63],[118,63],[124,63],[130,63],[135,63],[141,63],[146,63],[152,63],[158,63],[163,63],[169,63],[175,63],[180,63],[186,63],[191,63],[197,63], [11,64],[11,64],[122,64],[128,64],[134,64],[140,64],[145,64],[151,64],[157,64],[163,64],[169,64],[174,64],[180,64],[186,64],[192,64],[197,64],[204,64], [11,65],[12,65],[126,65],[132,65],[138,65],[144,65],[150,65],[156,65],[162,65],[168,65],[174,65],[180,65],[186,65],[192,65],[198,65],[204,65],[210,65], [11,66],[12,66],[130,66],[136,66],[142,66],[148,66],[155,66],[161,66],[167,66],[173,66],[179,66],[186,66],[192,66],[198,66],[204,66],[210,66],[216,66], [12,67],[12,67],[134,67],[140,67],[146,67],[153,67],[159,67],[166,67],[172,67],[178,67],[185,67],[191,67],[198,67],[204,67],[211,67],[217,67],[223,67], [12,68],[13,68],[138,68],[144,68],[151,68],[158,68],[164,68],[171,68],[177,68],[184,68],[190,68],[197,68],[203,68],[210,68],[216,68],[223,68],[230,68], [12,69],[13,69],[142,69],[149,69],[155,69],[162,69],[169,69],[176,69],[182,69],[189,69],[196,69],[203,69],[209,69],[216,69],[223,69],[230,69],[236,69], [13,70],[13,70],[146,70],[153,70],[160,70],[167,70],[174,70],[181,70],[188,70],[195,70],[202,70],[209,70],[216,70],[222,70],[229,70],[236,70],[243,70], [13,71],[14,71],[150,71],[157,71],[165,71],[172,71],[179,71],[186,71],[193,71],[200,71],[208,71],[215,71],[222,71],[229,71],[236,71],[243,71],[250,71], [14,72],[14,72],[154,72],[162,72],[169,72],[177,72],[184,72],[191,72],[199,72],[206,72],[213,72],[221,72],[228,72],[235,72],[242,72],[250,72],[258,72], [14,73],[15,73],[159,73],[166,73],[174,73],[182,73],[189,73],[197,73],[204,73],[212,73],[219,73],[227,73],[235,73],[242,73],[250,73],[257,73],[265,73], [14,74],[15,74],[163,74],[171,74],[179,74],[186,74],[194,74],[202,74],[210,74],[218,74],[225,74],[233,74],[241,74],[249,74],[256,74],[264,74],[272,74], [15,75],[16,75],[168,75],[176,75],[184,75],[192,75],[200,75],[208,75],[216,75],[224,75],[232,75],[240,75],[248,75],[256,75],[264,75],[272,75],[279,75], [15,76],[16,76],[172,76],[180,76],[189,76],[197,76],[205,76],[213,76],[221,76],[230,76],[238,76],[246,76],[254,76],[263,76],[271,76],[279,76],[287,76]]

BMI_features = [ "NOR", "NOR", "NOR", "NOR", "NOR", "NOR", "OVE", "OVE", "OVE", "OVE", "OVE", "OBE", "OBE", "OBE", "OBE", "OBE", "OBE", "NOR", "NOR", "NOR", "NOR", "NOR", "NOR", "OVE", "OVE", "OVE", "OVE", "OVE", "OBE", "OBE", "OBE", "OBE", "OBE", "OBE", "NOR", "NOR", "NOR", "NOR", "NOR", "NOR", "OVE", "OVE", "OVE", "OVE", "OVE", "OBE", "OBE", "OBE", "OBE", "OBE", "OBE", "NOR", "NOR", "NOR", "NOR", "NOR", "NOR", "OVE", "OVE", "OVE", "OVE", "OVE", "OBE", "OBE", "OBE", "OBE", "OBE", "OBE", "NOR", "NOR", "NOR", "NOR", "NOR", "NOR", "OVE", "OVE", "OVE", "OVE", "OVE", "OBE", "OBE", "OBE", "OBE", "OBE", "OBE", "NOR", "NOR", "NOR", "NOR", "NOR", "NOR", "OVE", "OVE", "OVE", "OVE", "OVE", "OBE", "OBE", "OBE", "OBE", "OBE", "OBE", "NOR", "NOR", "NOR", "NOR", "NOR", "NOR", "OVE", "OVE", "OVE", "OVE", "OVE", "OBE", "OBE", "OBE", "OBE", "OBE", "OBE", "NOR", "NOR", "NOR", "NOR", "NOR", "NOR", "OVE", "OVE", "OVE", "OVE", "OVE", "OBE", "OBE", "OBE", "OBE", "OBE", "OBE", "NOR", "NOR", "NOR", "NOR", "NOR", "NOR", "OVE", "OVE", "OVE", "OVE", "OVE", "OBE", "OBE", "OBE", "OBE", "OBE", "OBE", "NOR", "NOR", "NOR", "NOR", "NOR", "NOR", "OVE", "OVE", "OVE", "OVE", "OVE", "OBE", "OBE", "OBE", "OBE", "OBE", "OBE", "NOR", "NOR", "NOR", "NOR", "NOR", "NOR", "OVE", "OVE", "OVE", "OVE", "OVE", "OBE", "OBE", "OBE", "OBE", "OBE", "OBE", "NOR", "NOR", "NOR", "NOR", "NOR", "NOR", "OVE", "OVE", "OVE", "OVE", "OVE", "OBE", "OBE", "OBE", "OBE", "OBE", "OBE", "NOR", "NOR", "NOR", "NOR", "NOR", "NOR", "OVE", "OVE", "OVE", "OVE", "OVE", "OBE", "OBE", "OBE", "OBE", "OBE", "OBE", "NOR", "NOR", "NOR", "NOR", "NOR", "NOR", "OVE", "OVE", "OVE", "OVE", "OVE", "OBE", "OBE", "OBE", "OBE", "OBE", "OBE", "NOR", "NOR", "NOR", "NOR", "NOR", "NOR", "OVE", "OVE", "OVE", "OVE", "OVE", "OBE", "OBE", "OBE", "OBE", "OBE", "OBE", "NOR", "NOR", "NOR", "NOR", "NOR", "NOR", "OVE", "OVE", "OVE", "OVE", "OVE", "OBE", "OBE", "OBE", "OBE", "OBE", "OBE", "NOR", "NOR", "NOR", "NOR", "NOR", "NOR", "OVE", "OVE", "OVE", "OVE", "OVE", "OBE", "OBE", "OBE", "OBE", "OBE", "OBE", "NOR", "NOR", "NOR", "NOR", "NOR", "NOR", "OVE", "OVE", "OVE", "OVE", "OVE", "OBE", "OBE", "OBE", "OBE", "OBE", "OBE"] 

#-------------------------------------------------------------------------------- 
# Lets find out if we are a normal, overweight, or obese
#-------------------------------------------------------------------------------- 

# Create identification tree from BMI table. 
clf = tree.DecisionTreeClassifier()
clf = clf.fit(Height_in_Weight_lbs_samples, BMI_features)

looping = True
while( looping ):
     weight = input("Enter your weight in lbs: ")
     if not weight:
         break

     height = input("Enter your height in inches: ") 
     if not height:
         break

     prediction = clf.predict([[weight,height]])
     print("It appears that you are:", prediction, "\r\n" )

#-------------------------------------------------------------------------------- 
# Generate a graph visualizing the trained decesion tree. 
#-------------------------------------------------------------------------------- 
# import graphviz 
# dot_data = tree.export_graphviz(clf, out_file=None) 
# graph = graphviz.Source(dot_data) 
# graph.render("BMI_Table", view=True) 

