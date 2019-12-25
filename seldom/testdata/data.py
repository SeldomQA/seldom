# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division, print_function, absolute_import
import re
import sys


first_names_female = list(set(re.split(r"\s+", """
mary patricia linda barbara elizabeth jennifer maria susan margaret dorothy lisa nancy karen betty helen
sandra donna carol ruth sharon michelle laura sarah kimberly deborah jessica shirley cynthia angela
melissa brenda amy anna rebecca virginia kathleen pamela martha debra amanda stephanie carolyn
christine marie janet catherine frances ann joyce diane alice julie heather teresa doris gloria
evelyn jean cheryl mildred katherine joan ashley judith rose janice kelly nicole judy christina
kathy theresa beverly denise tammy irene jane lori rachel marilyn andrea kathryn louise sara anne
jacqueline wanda bonnie julia ruby lois tina phyllis norma paula diana annie lillian emily robin
peggy crystal gladys rita dawn connie florence tracy edna tiffany carmen rosa cindy grace wendy
victoria edith kim sherry sylvia josephine thelma shannon sheila ethel ellen elaine marjorie carrie
charlotte monica esther pauline emma juanita anita rhonda hazel amber eva debbie april leslie clara
lucille jamie joanne eleanor valerie danielle megan alicia suzanne michele gail bertha darlene veronica
jill erin geraldine lauren cathy joann lorraine lynn sally regina erica beatrice dolores bernice
audrey yvonne annette june samantha marion dana stacy ana renee ida vivian roberta holly brittany
melanie loretta yolanda jeanette laurie katie kristen vanessa alma sue elsie beth jeanne vicki carla
tara rosemary eileen terri gertrude lucy tonya ella stacey wilma gina kristin jessie natalie agnes vera
willie charlene bessie delores melinda pearl arlene maureen colleen allison tamara joy georgia constance
lillie claudia jackie marcia tanya nellie minnie marlene heidi glenda lydia viola courtney marian stella
caroline dora jo vickie mattie terry maxine irma mabel marsha myrtle lena christy deanna patsy hilda
gwendolyn jennie nora margie nina cassandra leah penny kay priscilla naomi carole brandy olga billie
dianne tracey leona jenny felicia sonia miriam velma becky bobbie violet kristina toni misty mae shelly
daisy ramona sherri erika katrina claire lindsey lindsay geneva guadalupe belinda margarita sheryl cora
faye ada natasha sabrina isabel marguerite hattie harriet molly cecilia kristi brandi blanche sandy
rosie joanna iris eunice angie inez lynda madeline amelia alberta genevieve monique jodi janie maggie
kayla sonya jan lee kristine candace fannie maryann opal alison yvette melody luz susie olivia flora
shelley kristy mamie lula lola verna beulah antoinette candice juana jeannette pam kelli hannah whitney
bridget karla celia latoya patty shelia gayle della vicky lynne sheri marianne kara jacquelyn erma blanca
myra leticia pat krista roxanne angelica johnnie robyn francis adrienne rosalie alexandra brooke bethany
sadie bernadette traci jody kendra jasmine nichole rachael chelsea mable ernestine muriel marcella elena
krystal angelina nadine kari estelle dianna paulette lora mona doreen rosemarie angel desiree antonia
hope ginger janis betsy christie freda mercedes meredith lynette teri cristina eula leigh meghan sophia
eloise rochelle gretchen cecelia raquel henrietta alyssa jana kelley gwen kerry jenna tricia laverne
olive alexis tasha silvia elvira casey delia sophie kate patti lorena kellie sonja lila lana darla may
mindy essie mandy lorene elsa josefina jeannie miranda dixie lucia marta faith lela johanna shari camille
tami shawna elisa ebony melba ora nettie tabitha ollie jaime winifred kristie marina alisha aimee rena
myrna marla tammie latasha bonita patrice ronda sherrie addie francine deloris stacie adriana cheri shelby
abigail celeste jewel cara adele rebekah lucinda dorthy chris effie trina reba shawn sallie aurora lenora
etta lottie kerri trisha nikki estella francisca josie tracie marissa karin brittney janelle lourdes
laurel helene fern elva corinne kelsey ina bettie elisabeth aida caitlin ingrid iva eugenia christa
goldie cassie maude jenifer therese frankie dena lorna janette latonya candy morgan consuelo tamika
rosetta debora cherie polly dina jewell fay jillian dorothea nell trudy esperanza patrica kimberley shanna
helena carolina cleo stefanie rosario ola janine mollie lupe alisa lou maribel susanne bette susana elise
cecile isabelle lesley jocelyn paige joni rachelle leola daphne alta ester petra graciela imogene jolene
keisha lacey glenna gabriela keri ursula lizzie kirsten shana adeline mayra jayne jaclyn gracie sondra
carmela marisa rosalind charity tonia beatriz marisol clarice jeanine sheena angeline frieda lily robbie
shauna millie claudette cathleen angelia gabrielle autumn katharine summer jodie staci lea christi jimmie
justine elma luella margret dominique socorro rene martina margo mavis callie bobbi maritza lucile leanne
jeannine deana aileen lorie ladonna willa manuela gale selma dolly sybil abby lara dale ivy dee winnie
marcy luisa jeri magdalena ofelia meagan audra matilda leila cornelia bianca simone bettye randi virgie
latisha barbra georgina eliza leann bridgette rhoda haley adela nola bernadine flossie ila greta ruthie
nelda minerva lilly terrie letha hilary estela valarie brianna rosalyn earline catalina ava mia clarissa
lidia corrine alexandria concepcion tia sharron rae dona ericka jami elnora chandra lenore neva marylou
melisa tabatha serena avis allie sofia jeanie odessa nannie harriett loraine penelope milagros emilia
benita allyson ashlee tania tommie esmeralda karina eve pearlie zelma malinda noreen tameka saundra hillary
amie althea rosalinda jordan lilia alana gay clare alejandra elinor michael lorrie jerri darcy earnestine
carmella taylor noemi marcie liza annabelle louisa earlene mallory carlene nita selena tanisha katy julianne
john lakisha edwina maricela margery kenya dollie roxie roslyn kathrine nanette charmaine lavonne ilene
kris tammi suzette corine kaye jerry merle chrystal lina deanne lilian juliana aline luann kasey maryanne
evangeline colette melva lawanda yesenia nadia madge kathie eddie ophelia valeria nona mitzi mari georgette
claudine fran alissa roseann lakeisha susanna reva deidre chasity sheree carly james elvia alyce deirdre
gena briana araceli katelyn rosanne wendi tessa berta marva imelda marietta marci leonor arline sasha
madelyn janna juliette deena aurelia josefa augusta liliana young christian lessie amalia savannah
anastasia vilma natalia rosella lynnette corina alfreda leanna carey amparo coleen tamra aisha wilda
karyn cherry queen maura mai evangelina rosanna hallie erna enid mariana lacy juliet jacklyn freida
madeleine mara hester cathryn lelia casandra bridgett angelita jannie dionne annmarie katina beryl phoebe
millicent katheryn diann carissa maryellen liz lauri helga gilda adrian rhea marquita hollie tisha tamera
angelique francesca britney kaitlin lolita florine rowena reyna twila fanny janell ines concetta bertie
alba brigitte alyson vonda pansy elba noelle letitia kitty deann brandie louella leta felecia sharlene
lesa beverley robert isabella herminia terra celina

Abbie-Leigh Abbie-Louise Abbie-May Aimee-Grace Aimee-Jo Aimee-Lea Aimee-Lee Aimee-Leigh
Aimee-Louise Aimee-Rose Alesha-Mae Alexa-Rose Alice-Mae Alice-May Alicia-Mae Alicia-May Alisha-May
Alisha-Rose Alissa-Mae Alyssa-Mae Amber-Leigh Amber-Louise Amber-Mae Amber-Rose Amelia-Grace Amelia-Jane
Amelia-Jayne Amelia-Mae Amelia-Mai Amelia-Rose Amelie-Grace Amelie-Rose Amie-Leigh Amy-Grace Amy-Jane
Amy-Jayne Amy-Jo Amy-Lea Amy-Lee Amy-Leigh Amy-Lou Amy-Louise Amy-May Amy-Rose Ana-Maria Angel-Louise Angel-Mae
Angel-Mai Angel-Marie Angel-Rose Anna-Leigh Anna-Louise Anna-Mae Anna-Maria Anna-Marie Anna-May
Anna-Rose Anna-Sophia Anne-Marie Annie-Mae Annie-Mai Annie-May Annie-Rose Ann-Marie Anya-Rose April-Rose
Autumn-Rose Ava-Grace Ava-Jane Ava-Jo Ava-Leigh Ava-Lily Ava-Louise Ava-Mae Ava-Mai Ava-Marie Ava-May
Ava-Nicole Ava-Rose Ava-Sophia Bailey-Mae Bailey-Rae Bella-Rose Bethany-Ann Bethany-Rose Billie-Jean Billie-Jo
Billie-Mae Billie-Rose Bobbie-Jo Bobbie-Leigh Bobbi-Jo Bonnie-May Brodie-Leigh Brooke-Elise Brooke-Leigh
Brooke-Louise Cara-Louise Carol-Ann Carrie-Ann Carrie-Anne Casey-Jayne Casey-Leigh Casey-Mae Casey-Marie
Casey-May Charlie-Mae Charlie-May Charlotte-Rose Chloe-Ann Chloe-Anne Chloe-Jade Chloe-Leigh Chloe-Louise Chloe-Mae
Chloe-Mai Chloe-Marie Chloe-May Chloe-Rose Chloe-Sophia Codie-Leigh Connie-Mae Connie-Rose Courtney-Jade
Courtney-Leigh Courtney-Rose Daisy-Ann Daisy-Boo Daisy-Leigh Daisy-Lou Daisy-Mae Daisy-Mai Daisy-May
Daisy-Rose Darcey-Leigh Darcey-May Darcie-Mae Darcie-Rose Darci-Leigh Darci-Rose Darcy-Mae Darcy-May
Demi-Elise Demi-Jo Demi-Lea Demi-Lee Demi-Leigh Demi-Lou Demi-Louise Demi-Mai Demi-Marie Demi-May Demi-Rae
Demi-Rose Destiny-Mai Dollie-Mai Ebony-Grace Ebony-Mae Ebony-Mai Ebony-Rose Eden-Rose Edie-Mae Eliza-Rose
Ella-Grace Ella-Jade Ella-Jai Ella-Jane Ella-Jayne Ella-Louise Ella-Mae Ella-Mai Ella-Marie Ella-May Ella-Rae
Ella-Rose Elle-Louise Elle-Mae Elle-Mai Elle-May Ellie-Ann Ellie-Anne Ellie-Grace Ellie-Jane Ellie-Jay Ellie-Jayne
Ellie-Jo Ellie-Leigh Ellie-Louise Ellie-Mae Ellie-Mai Ellie-Marie Ellie-May Ellie-Rae Ellie-Rose Elli-Mae
Elli-Mai Elsie-Mae Elsie-May Elsie-Rose Emily-Ann Emily-Anne Emily-Grace Emily-Jane Emily-Jayne Emily-Louise
Emily-Mae Emily-Mai Emily-May Emily-Rose Emma-Jane Emma-Jayne Emma-Leigh Emma-Louise Emmie-Lou Erin-Mae
Eva-Mae Eva-Maria Eva-Marie Eva-May Eva-Rose Evelyn-Rose Evie-Anne Evie-Grace Evie-Jane Evie-Jayne Evie-Jean
Evie-Jo Evie-Leigh Evie-Louise Evie-Mae Evie-Mai Evie-Marie Evie-May Evie-Rose Faatimah-Zahra Faith-Marie Felicity-Rose
Frankie-Lee Frankie-Leigh Freya-Grace Freya-Leigh Freya-Louise Freya-Mae Freya-Mai Freya-May Georgia-Leigh
Georgia-Mae Georgia-Mai Georgia-May Georgia-Rose Georgie-May Grace-Lily Gracie-Ann Gracie-Jane Gracie-Jayne
Gracie-Lea Gracie-Lee Gracie-Leigh Gracie-Lou Gracie-Mae Gracie-Mai Gracie-May Gracie-Rose Hailie-Jade Halle-Mae
Halle-Mai Hallie-Mae Hannah-Louise Hannah-Mae Hannah-May Hollie-Ann Hollie-Grace Hollie-Louise Hollie-Mae
Hollie-Mai Hollie-May Hollie-Rose Holly-Ann Holly-Louise Holly-Mae Holly-Mai Holly-Marie Holly-May Holly-Rose
Honey-Mae India-Rose Indie-Rose Isabella-Grace Isabella-Mae Isabella-Rose Isabelle-Rose Isla-Mae
Isla-May Isla-Rose Isobel-Rose Izzy-Mai Jaimee-Lee Jaimee-Leigh Jaime-Leigh Jamie-Lea Jamie-Lee Jamie-Leigh
Jamie-Louise Jasmine-Rose Jaycee-Leigh Jayme-Leigh Jaymie-Leigh Jessica-Jane Jessica-Leigh Jessica-Lily
Jessica-Louise Jessica-Mae Jessica-Mai Jessica-May Jessica-Paige Jessica-Rose Jessica-Taylor Jessie-Mai
Jodie-Leigh Josie-May Julie-Ann Kacey-Lee Kacey-Leigh Kacey-Louise Kacey-May Kacie-Ann Kacie-Leigh Kacie-Mae
Kacie-May Kaci-Leigh Kaci-Louise Kaci-Mae Kaci-May Kadie-Leigh Kady-Leigh Kara-Louise Kasey-Leigh Kate-Lynn
Katie-Ann Katie-Jane Katie-Jayne Katie-Jo Katie-Lee Katie-Leigh Katie-Louise Katie-Mae Katie-Mai Katie-Marie
Katie-May Katie-Rose Katy-Leigh Kaycee-Leigh Kaycie-Leigh Kaydee-Leigh Kaydie-Leigh Kayla-Mae Kayla-Mai
Kayla-May Kayla-Rose Kay-Leigh Kayleigh-Ann Kayleigh-May Keira-Lee Keira-Leigh Keira-Louise Keira-Marie Kelly-Anne
Kelsie-Ann Kerry-Ann Kerry-Anne Kiara-Leigh Kiera-Leigh Kiera-Louise Kira-Leigh Kitty-Rose Kyla-Mae Kyla-May
Kyra-Lea Kyra-Leigh Kyra-Louise Lacey-Ann Lacey-Anne Lacey-Jade Lacey-Jane Lacey-Jay Lacey-Jo Lacey-Leigh
Lacey-Louise Lacey-Mae Lacey-Mai Lacey-Marie Lacey-May Lacey-Rose Lacie-Leigh Lacie-Mae Lacie-Mai Lacie-May
Laci-Mai Laila-Mai Laila-Marie Laila-Rose Layla-Faye Layla-Grace Layla-Louise Layla-Mae Layla-Mai Layla-May
Layla-Rae Layla-Rose Leah-Louise Leah-Mae Leah-Marie Leah-May Leah-Rose Lexi-Ann Lexi-Anne Lexie-Grace Lexie-Jay
Lexie-Jayne Lexie-Jo Lexie-Leigh Lexie-Lou Lexie-Mae Lexie-Mai Lexie-May Lexie-Rae Lexie-Rose Lexi-Grace Lexi-Jane
Lexi-Jayne Lexi-Jo Lexi-Lea Lexi-Leigh Lexi-Lou Lexi-Louise Lexi-Mae Lexi-Mai Lexi-Marie Lexi-May Lexi-Rose Libby-Jane
Libby-Louise Libby-Mae Libby-Mai Libby-May Libby-Rose Liberty-Grace Lila-Grace Lilah-Grace Lila-Rose Lili-Mae
Lili-Mai Lili-May Lillie-Ann Lillie-Anne Lillie-Mae Lillie-Mai Lillie-Marie Lillie-May Lillie-Rae Lillie-Rose Lilli-Mae
Lilli-Mai Lilli-Rose Lilly-Ann Lilly-Anna Lilly-Anne Lilly-Belle Lilly-Ella Lilly-Grace Lilly-Jade Lilly-Jane
Lilly-Jayne Lilly-Jean Lilly-Jo Lilly-Louise Lilly-Mae Lilly-Mai Lilly-Marie Lilly-May Lilly-Rae Lilly-Rose Lilly-Sue
Lily-Ann Lily-Anna Lily-Anne Lily-Belle Lily-Beth Lily-Ella Lily-Faye Lily-Grace Lily-Jade Lily-Jane Lily-Jay
Lily-Jayne Lily-Jo Lily-Louise Lily-Mae Lily-Mai Lily-Marie Lily-May Lily-Rae Lily-Rose Lily-Sue Lisa-Marie Lola-Grace
Lola-Jo Lola-Louise Lola-Mae Lola-Mai Lola-May Lola-Rose Lucie-Jo Lucie-Mae Lucy-Ann Lucy-Anne Lucy-Jane Lucy-Jo
Lucy-Louise Lucy-Mae Lucy-May Lucy-Rose Lydia-Mae Lyla-Grace Lyla-Rose Macey-Leigh Macie-Lea Macie-Leigh Macie-Rose Macy-Jo
Maddie-Rose Maddison-Grace Maddison-Rose Madison-Grace Madison-Leigh Maisie-Ann Maisie-Grace Maisie-Jane Maisie-Jayne
Maisie-Jo Maisie-Lee Maisie-Leigh Maisie-Lou Maisie-Mae Maisie-May Maisie-Rose Maisy-Jane Maisy-May Mary-Ann
Mary-Anne Mary-Ellen Mary-Jane Mary-Jayne Mary-Kate Mary-Rose Matilda-Rose Mckenzie-Leigh Megan-Grace Megan-Leigh
Megan-Rose Melody-Rose Mia-Ann Mia-Grace Mia-Jade Mia-Jayne Mia-Jo Mia-Leigh Mia-Lily Mia-Louise Mia-Nicole Mia-Rose
Miley-Grace Miley-Jo Miley-Mae Miley-Mai Miley-Rae Miley-Rose Milli-Ann Millie-Ann Millie-Anne Millie-Grace Millie-Jayne
Millie-Jo Millie-Mae Millie-Mai Millie-May Millie-Rose Milly-May Milly-Rose Mollie-Ann Mollie-Louise Mollie-Mae
Mollie-May Mollie-Rose Molly-Ann Molly-Anne Molly-Jo Molly-Mae Molly-Mai Molly-May Molly-Rose Morgan-Leigh
Mya-Louise Mya-Rose Nancy-May Nevaeh-Rose Noor-Fatima Olivia-Grace Olivia-Jane Olivia-Leigh Olivia-Mae
Olivia-Mai Olivia-may Olivia-Paige Olivia-Rose Paige-Marie Phoebe-Lee Phoebe-Louise Phoebe-Rose Poppy-Ann
Poppy-Anne Poppy-Grace Poppy-Jo Poppy-Mae Poppy-Mai Poppy-May Poppy-Rose Ronnie-May Rose-Marie Rosie-Ann
Rosie-Leigh Rosie-Mae Rosie-Mai Rosie-May Rubie-Leigh Rubie-Mae Rubie-Mai Ruby-Ann Ruby-Anne Ruby-Blu Ruby-Grace
Ruby-Jane Ruby-Jean Ruby-Jo Ruby-Lea Ruby-Lee Ruby-Leigh Ruby-Lou Ruby-Louise Ruby-Mae Ruby-Mai Ruby-Marie
Ruby-May Ruby-Rae Ruby-Rose Sadie-Rose Sammi-Jo Sammy-Jo Sarah-Jane Sarah-Jayne Sarah-Louise Scarlet-Rose
Scarlett-Louise Scarlett-Mae Scarlett-Marie Scarlett-Rose Seren-Louise Shannon-Louise Shayla-Louise Shayla-Rae
Sienna-Grace Sienna-Lee Sienna-Leigh Sienna-Mae Sienna-Marie Sienna-May Sienna-Rose Skye-Louise Skye-Marie Skyla-Mae
Skyla-Mai Sky-Louise Sophia-Rose Sophie-Ann Sophie-Anne Sophie-Ella Sophie-Grace Sophie-Jane Sophie-Leigh
Sophie-Louise Sophie-Mae Sophie-Mai Sophie-Marie Sophie-May Sophie-Rose Stevie-Leigh Summer-Jade Summer-Jayne Summer-Lea
Summer-Leigh Summer-Lily Summer-Louise Summer-Mae Summer-Marie Summer-May Summer-Rose Sydney-Rose Tallulah-Mae
Taylor-Ann Taylor-Grace Taylor-Jane Taylor-Jay Taylor-Leigh Taylor-Louise Taylor-Mae Taylor-May Taylor-Rose
Tegan-Louise Tia-Leigh Tia-Louise Tia-Mae Tia-Mai Tia-Marie Tia-May Tia-Rae Tia-Rose Tiana-Leigh Tiana-Marie
Tianna-Marie Tiffany-Marie Tiger-Lilly Tiger-Lily Tillie-Mae Tillie-Mai Tilly-Mae Tilly-Mai Tilly-Marie Tilly-May
Tilly-Rose Toni-Ann Toni-Leigh Toni-Marie Tori-Lee Tori-Leigh Umme-Haani Violet-Rose Willow-Rose 

Toa'ale Hau'oli O'Brie God'iss Domi'nique La'tanya Rah'Nee A'merika Shau'Nay Mich'ele
N'cole A'Brianna Ma'Kayla Sha'tyana Zy'shonne November'Lashae Ja'Kingston and Ke'Shawn D'nasia
An'Gelina O'Livia Dan'Yelle Ky'Lee Rach'El Cie'Rrea Sh'nia Day'quandray Don'ta'ja Fiaavd'e I'Lanny Day'twain La'tko
L'Cole Sei'Jearr Ta'Quwereus 
A'jA Anah'reya A'Majena Be'aJa Cier'rrea D'aSiyahna D'Kota E'ryn I'Zeyonna Ja'genevia JaKeil'a Ta-Shay
Ja'mya Jane't Kei'Lee Ken'yel K'le Mi'Angel N'finique Sanai' Sh'nia Syn'Cere Syri'yah Ti-Leigh'yah
Zae'kee Zy'Erica Zy'rreah 
""".strip())))


first_names_male = list(set(re.split(r"\s+", """
aaron abdul abe abel abraham abram adalberto adam adan adolfo adolph adrian agustin ahmad ahmed al alan
albert alberto alden aldo alec alejandro alex alexander alexis alfonso alfonzo alfred alfredo ali allan
allen alonso alonzo alphonse alphonso alton alva alvaro alvin amado ambrose amos anderson andre andrea
andreas andres andrew andy angel angelo anibal anthony antione antoine anton antone antonia antonio
antony antwan archie arden ariel arlen arlie armand armando arnold arnoldo arnulfo aron arron art arthur
arturo asa ashley aubrey august augustine augustus aurelio austin avery barney barrett barry bart barton
basil beau ben benedict benito benjamin bennett bennie benny benton bernard bernardo bernie berry bert
bertram bill billie billy blaine blair blake bo bob bobbie bobby booker boris boyce boyd brad bradford
bradley bradly brady brain branden brandon brant brendan brendon brent brenton bret brett brian brice
britt brock broderick brooks bruce bruno bryan bryant bryce bryon buck bud buddy buford burl burt burton
buster byron caleb calvin cameron carey carl carlo carlos carlton carmelo carmen carmine carol carrol
carroll carson carter cary casey cecil cedric cedrick cesar chad chadwick chance chang charles charley
charlie chas chase chauncey chester chet chi chong chris christian christoper christopher chuck chung
clair clarence clark claud claude claudio clay clayton clement clemente cleo cletus cleveland cliff
clifford clifton clint clinton clyde cody colby cole coleman colin collin colton columbus connie conrad
cordell corey cornelius cornell cortez cory courtney coy craig cristobal cristopher cruz curt curtis
cyril cyrus dale dallas dalton damian damien damion damon dan dana dane danial daniel danilo dannie danny
dante darell daren darin dario darius darnell daron darrel darrell darren darrick darrin darron darryl
darwin daryl dave david davis dean deandre deangelo dee del delbert delmar delmer demarcus demetrius denis
dennis denny denver deon derek derick derrick deshawn desmond devin devon dewayne dewey dewitt dexter
dick diego dillon dino dion dirk domenic domingo dominic dominick dominique don donald dong donn donnell
donnie donny donovan donte dorian dorsey doug douglas douglass doyle drew duane dudley duncan dustin
dusty dwain dwayne dwight dylan earl earle earnest ed eddie eddy edgar edgardo edison edmond edmund
edmundo eduardo edward edwardo edwin efrain efren elbert elden eldon eldridge eli elias elijah eliseo
elisha elliot elliott ellis ellsworth elmer elmo eloy elroy elton elvin elvis elwood emanuel emerson
emery emil emile emilio emmanuel emmett emmitt emory enoch enrique erasmo eric erich erick erik erin
ernest ernesto ernie errol ervin erwin esteban ethan eugene eugenio eusebio evan everett everette ezekiel
ezequiel ezra fabian faustino fausto federico felipe felix felton ferdinand fermin fernando fidel filiberto
fletcher florencio florentino floyd forest forrest foster frances francesco francis francisco frank
frankie franklin franklyn fred freddie freddy frederic frederick fredric fredrick freeman fritz gabriel
gail gale galen garfield garland garret garrett garry garth gary gaston gavin gayle gaylord genaro gene
geoffrey george gerald geraldo gerard gerardo german gerry gil gilbert gilberto gino giovanni giuseppe
glen glenn gonzalo gordon grady graham graig grant granville greg gregg gregorio gregory grover guadalupe
guillermo gus gustavo guy hai hal hank hans harlan harland harley harold harris harrison harry harvey
hassan hayden haywood heath hector henry herb herbert heriberto herman herschel hershel hilario hilton
hipolito hiram hobert hollis homer hong horace horacio hosea houston howard hoyt hubert huey hugh hugo
humberto hung hunter hyman ian ignacio ike ira irvin irving irwin isaac isaiah isaias isiah isidro ismael
israel isreal issac ivan ivory jacinto jack jackie jackson jacob jacques jae jaime jake jamaal jamal jamar
jame jamel james jamey jamie jamison jan jared jarod jarred jarrett jarrod jarvis jason jasper javier jay
jayson jc jean jed jeff jefferey jefferson jeffery jeffrey jeffry jerald jeramy jere jeremiah jeremy
jermaine jerold jerome jeromy jerrell jerrod jerrold jerry jess jesse jessie jesus jewel jewell jim jimmie
jimmy joan joaquin jody joe joel joesph joey john johnathan johnathon johnie johnnie johnny johnson jon
jonah jonas jonathan jonathon jordan jordon jorge jose josef joseph josh joshua josiah jospeh josue juan
jude judson jules julian julio julius junior justin kareem karl kasey keenan keith kelley kelly kelvin
ken kendall kendrick keneth kenneth kennith kenny kent kenton kermit kerry keven kevin kieth kim king kip
kirby kirk korey kory kraig kris kristofer kristopher kurt kurtis kyle lacy lamar lamont lance landon lane
lanny larry lauren laurence lavern laverne lawerence lawrence lazaro leandro lee leif leigh leland lemuel
len lenard lenny leo leon leonard leonardo leonel leopoldo leroy les lesley leslie lester levi lewis
lincoln lindsay lindsey lino linwood lionel lloyd logan lon long lonnie lonny loren lorenzo lou louie
louis lowell loyd lucas luciano lucien lucio lucius luigi luis luke lupe luther lyle lyman lyndon lynn
lynwood mac mack major malcolm malcom malik man manual manuel marc marcel marcelino marcellus marcelo
marco marcos marcus margarito maria mariano mario marion mark markus marlin marlon marquis marshall
martin marty marvin mary mason mathew matt matthew maurice mauricio mauro max maximo maxwell maynard
mckinley mel melvin merle merlin merrill mervin micah michael michal michale micheal michel mickey miguel
mike mikel milan miles milford millard milo milton minh miquel mitch mitchel mitchell modesto mohamed
mohammad mohammed moises monroe monte monty morgan morris morton mose moses moshe murray myles myron
napoleon nathan nathanael nathanial nathaniel neal ned neil nelson nestor neville newton nicholas nick
nickolas nicky nicolas nigel noah noble noe noel nolan norbert norberto norman normand norris numbers
octavio odell odis olen olin oliver ollie omar omer oren orlando orval orville oscar osvaldo oswaldo
otha otis otto owen pablo palmer paris parker pasquale pat patricia patrick paul pedro percy perry pete
peter phil philip phillip pierre porfirio porter preston prince quentin quincy quinn quintin quinton
rafael raleigh ralph ramiro ramon randal randall randell randolph randy raphael rashad raul ray rayford
raymon raymond raymundo reed refugio reggie reginald reid reinaldo renaldo renato rene reuben rex rey
reyes reynaldo rhett ricardo rich richard richie rick rickey rickie ricky rico rigoberto riley rob robbie
robby robert roberto robin robt rocco rocky rod roderick rodger rodney rodolfo rodrick rodrigo rogelio
roger roland rolando rolf rolland roman romeo ron ronald ronnie ronny roosevelt rory rosario roscoe rosendo
ross roy royal royce ruben rubin rudolf rudolph rudy rueben rufus rupert russ russel russell rusty ryan
sal salvador salvatore sam sammie sammy samual samuel sandy sanford sang santiago santo santos saul scot
scott scottie scotty sean sebastian sergio seth seymour shad shane shannon shaun shawn shayne shelby
sheldon shelton sherman sherwood shirley shon sid sidney silas simon sol solomon son sonny spencer stacey
stacy stan stanford stanley stanton stefan stephan stephen sterling steve steven stevie stewart stuart
sung sydney sylvester tad tanner taylor ted teddy teodoro terence terrance terrell terrence terry thad
thaddeus thanh theo theodore theron thomas thurman tim timmy timothy titus tobias toby tod todd tom tomas
tommie tommy toney tony tory tracey tracy travis trent trenton trevor trey trinidad tristan troy truman
tuan ty tyler tyree tyrell tyron tyrone tyson ulysses val valentin valentine van vance vaughn vern vernon
vicente victor vince vincent vincenzo virgil virgilio vito von wade waldo walker wallace wally walter
walton ward warner warren waylon wayne weldon wendell werner wes wesley weston whitney wilber wilbert
wilbur wilburn wiley wilford wilfred wilfredo will willard william williams willian willie willis willy
wilmer wilson wilton winford winfred winston wm woodrow wyatt xavier yong young zachariah zachary zachery
zack zackary zane

Aaron-James Abdul-Aziz Abdul-Hadi Abdul-Malik Abdul-Raheem Abdul-Rahim Abdul-Rahman Abdul-Rehman Abdul-Sami
Abdur-Raheem Abdur-Rahim Abdus-Samad Abu-Bakar Abu-Bakr Abu-Sufyan Aiden-James Aiden-Lee A-Jay Al-Amin
Alexander-James Alfie-Jack Alfie-Jai Alfie-James Alfie-Jay Alfie-Joe Alfie-John Alfie-Lee Alfie-Ray Andrew-James
Archie-Jay Archie-Lee Ashton-Lee Aston-Lee Bailey-James Bailey-Rae Billy-Jay Billy-Joe Billy-Lee Billy-Ray
Bobby-Jack Bobby-James Bobby-Jay Bobby-Joe Bobby-Lee Braiden-Lee Brandon-Lee Brogan-Lee Callum-James Cameron-James
Cameron-Jay Charlie-Dean Charlie-George Charlie-James Charlie-Jay Charlie-Joe Charlie-Ray C-Jay Cody-James
Cody-Jay Cody-Lee Conner-Lee Connor-James Connor-Jay Connor-Lee Corey-James Corey-Lee Daniel-James Daniel-Junior
Danny-Lee David-James Dylan-James Ethan-James Ethan-Lee Finley-James Frankie-Lee Freddie-Jay Freddie-Lee Harley-James
Harley-Jay Harley-Joe Harley-John Harley-Ray Harrison-Lee Harry-George Harry-James Harry-Lee Harvey-James Harvey-Jay
Harvey-Lee Harvey-Leigh Hayden-Lee Henry-James Jacob-James Jacob-Lee Jaiden-Lee James-Dean Jamie-Lee Jason-James
Jay-D Jaydan-Lee Jayden-James Jayden-Jay Jayden-John Jayden-Lee Jayden-Leigh Jay-Jay Jay-Junior Jay-Lee Jean-Paul
Jean-Pierre Jesse-James J-Jay Joe-Lewis Johnny-Lee John-Joseph John-Paul Jon-Paul Jordan-Lee Joseph-James Joshua-James
Joshua-Jay Junior-Jay Justin-Lee Kaiden-Lee Kal-El Kayden-Lee Keegan-Lee Kenzie-James Kenzie-Jay Kenzie-Lee
Kieran-Lee K-Jay Layton-James Layton-Lee Lee-Jay Leighton-James Leo-James Leon-Junior Levi-James Levi-Jay
Lewis-James Lewis-Lee Liam-James L-Jay Logan-James Logan-Jay Logan-Lee Louie-Jay Lucas-Jack Lucas-James
Lucas-Jay Mackenzie-Lee Marley-Lee Marley-Rae Mason-James Mason-Jay Mason-Lee Mckenzie-Jay Mckenzie-Lee
Michael-John Michael-Lee Mohamed-Amin Mohammed-Ibrahim Mohammed-Mustafa Muhammah-Ali Muhammad-Ibrahim Muhammad-Yusef
Nathan-Lee Oliver-James Owen-James Peter-Junior Ricky-Junior Riley-James Riley-Jay Riley-Joe Ronnie-Lee Russell-James
Ryan-James Ryan-Lee Saif-Ullah Sean-Paul Sonny-Lee Taylor-Jake Taylor-James Taylor-Jay Taylor-Lee Tee-Jay Thomas-James
Thomas-Jay Thomas-Lee T-Jay Tommy-Lee Tyler-Jack Tyler-Jake Tyler-James Tyler-Jay Tyler-Joe Tyler-Lee

D'Angelo De'wayne D'Juan X'Zavier Cha'Nce Jer'Miah J'siah Cam'Ron Chanze'es D'Jon D'Monie 
O'Jai O'Merion Q'ndell R'Son Ja'sheem Ted'Quarius Xa'Viance za'Veann Z'Jayden R'yaire 
""".strip())))


last_names = list(set(re.split(r"\s+", """
smith johnson williams brown jones miller davis garcia rodriguez wilson martinez anderson taylor thomas
hernandez moore martin jackson thompson white lopez lee gonzalez harris clark lewis robinson walker
perez hall young allen sanchez wright king scott green baker adams nelson hill ramirez campbell mitchell
roberts carter phillips evans turner torres parker collins edwards stewart flores morris nguyen murphy
rivera cook rogers morgan peterson cooper reed bailey bell gomez kelly howard ward cox diaz richardson
wood watson brooks bennett gray james reyes cruz hughes price myers long foster sanders ross morales
powell sullivan russell ortiz jenkins gutierrez perry butler barnes fisher henderson coleman simmons
patterson jordan reynolds hamilton graham kim gonzales alexander ramos wallace griffin west cole hayes
chavez gibson bryant ellis stevens murray ford marshall owens mcdonald harrison ruiz kennedy wells
alvarez woods mendoza castillo olson webb washington tucker freeman burns henry vasquez snyder simpson
crawford jimenez porter mason shaw gordon wagner hunter romero hicks dixon hunt palmer robertson black
holmes stone meyer boyd mills warren fox rose rice moreno schmidt patel ferguson nichols herrera medina
ryan fernandez weaver daniels stephens gardner payne kelley dunn pierce arnold tran spencer peters
hawkins grant hansen castro hoffman hart elliott cunningham knight bradley carroll hudson duncan
armstrong berry andrews johnston ray lane riley carpenter perkins aguilar silva richards willis matthews
chapman lawrence garza vargas watkins wheeler larson carlson harper george greene burke guzman morrison
munoz jacobs obrien lawson franklin lynch bishop carr salazar austin mendez gilbert jensen williamson
montgomery harvey oliver howell dean hanson weber garrett sims burton fuller soto mccoy welch chen
schultz walters reid fields walsh little fowler bowman davidson may day schneider newman brewer lucas
holland wong banks santos curtis pearson delgado valdez pena rios douglas sandoval barrett hopkins keller
guerrero stanley bates alvarado beck ortega wade estrada contreras barnett caldwell santiago lambert
powers chambers nunez craig leonard lowe rhodes byrd gregory shelton frazier becker maldonado fleming
vega sutton cohen jennings parks mcdaniel watts barker norris vaughn vazquez holt schwartz steele benson
neal dominguez horton terry wolfe hale lyons graves haynes miles park warner padilla bush thornton
mccarthy mann zimmerman erickson fletcher mckinney page dawson joseph marquez reeves klein espinoza
baldwin moran love robbins higgins ball cortez le griffith bowen sharp cummings ramsey hardy swanson
barber acosta luna chandler blair daniel cross simon dennis oconnor quinn gross navarro moss fitzgerald
doyle mclaughlin rojas rodgers stevenson singh yang figueroa harmon newton paul manning garner mcgee
reese francis burgess adkins goodman curry brady christensen potter walton goodwin mullins molina webster
fischer campos avila sherman todd chang blake malone wolf hodges juarez gill farmer hines gallagher duran
hubbard cannon miranda wang saunders tate mack hammond carrillo townsend wise ingram barton mejia ayala
schroeder hampton rowe parsons frank waters strickland osborne maxwell chan deleon norman harrington
casey patton logan bowers mueller glover floyd hartman buchanan cobb french kramer mccormick clarke tyler
gibbs moody conner sparks mcguire leon bauer norton pope flynn hogan robles salinas yates lindsey lloyd
marsh mcbride owen solis pham lang pratt lara brock ballard trujillo shaffer drake roman aguirre morton
stokes lamb pacheco patrick cochran shepherd cain burnett hess li cervantes olsen briggs ochoa cabrera
velasquez montoya roth meyers cardenas fuentes weiss hoover wilkins nicholson underwood short carson
morrow colon holloway summers bryan petersen mckenzie serrano wilcox carey clayton poole calderon gallegos
greer rivas guerra decker collier wall whitaker bass flowers davenport conley houston huff copeland hood
monroe massey roberson combs franco larsen pittman randall skinner wilkinson kirby cameron bridges anthony
richard kirk bruce singleton mathis bradford boone abbott charles allison sweeney atkinson horn jefferson
rosales york christian phelps farrell castaneda nash dickerson bond wyatt foley chase gates vincent mathews
hodge garrison trevino villarreal heath dalton valencia callahan hensley atkins huffman roy boyer shields
lin hancock grimes glenn cline delacruz camacho dillon parrish oneill melton booth kane berg harrell pitts
savage wiggins brennan salas marks russo sawyer baxter golden hutchinson liu walter mcdowell wiley rich
humphrey johns koch suarez hobbs beard gilmore ibarra keith macias khan andrade ware stephenson henson
wilkerson dyer mcclure blackwell mercado tanner eaton clay barron beasley oneal preston small wu zamora
macdonald vance snow mcclain stafford orozco barry english shannon kline jacobson woodard huang kemp
mosley prince merritt hurst villanueva roach nolan lam yoder mccullough lester santana valenzuela winters
barrera leach orr berger mckee strong conway stein whitehead bullock escobar knox meadows solomon velez
odonnell kerr stout blankenship browning kent lozano bartlett pruitt buck barr gaines durham gentry
mcintyre sloan melendez rocha herman sexton moon hendricks rangel stark lowery hardin hull sellers ellison
calhoun gillespie mora knapp mccall morse dorsey weeks nielsen livingston leblanc mclean bradshaw glass
middleton buckley schaefer frost howe house mcintosh ho pennington reilly hebert mcfarland hickman noble
spears conrad arias galvan velazquez huynh frederick randolph cantu fitzpatrick mahoney peck villa michael
donovan mcconnell walls boyle mayer zuniga giles pineda pace hurley mays mcmillan crosby ayers case
bentley shepard everett pugh david mcmahon dunlap bender hahn harding acevedo raymond blackburn duffy
landry dougherty bautista shah potts arroyo valentine meza gould vaughan fry rush avery herring dodson
clements sampson tapia bean lynn crane farley cisneros benton ashley mckay finley best blevins friedman
moses sosa blanchard huber frye krueger bernard rosario rubio mullen benjamin haley chung moyer choi
horne yu s s woodward ali nixon hayden rivers estes mccarty richmond stuart maynard brandt oconnell hanna
sanford sheppard church burch levy rasmussen coffey ponce faulkner donaldson schmitt novak costa montes
booker cordova waller arellano maddox mata bonilla stanton compton kaufman dudley mcpherson beltran
dickson mccann villegas proctor hester cantrell daugherty cherry bray davila rowland levine madden spence
good irwin werner krause petty whitney baird hooper pollard zavala jarvis holden haas hendrix mcgrath
bird lucero terrell riggs joyce mercer rollins galloway duke odom andersen downs hatfield benitez archer
huerta travis mcneil hinton zhang hays mayo fritz branch mooney ewing ritter esparza frey braun gay
riddle haney kaiser holder chaney mcknight gamble vang cooley carney cowan forbes ferrell davies barajas
shea osborn bright cuevas bolton murillo lutz duarte kidd key cooke
""".strip())))


unicode_names = re.split(r'\s+', """
\u0410\u0431\u0440\u0430\u043c \u0410\u043b\u0435\u043a\u0441\u0430\u043d\u0434\u0440
\u0410\u043b\u0435\u043a\u0441\u0435\u0439 \u0410\u043b\u044c\u0431\u0435\u0440\u0442
\u0410\u043d\u0430\u0442\u043e\u043b\u0438\u0439 \u0410\u043d\u0434\u0440\u0435\u0439
\u0410\u043d\u0442\u043e\u043d \u0410\u0440\u043a\u0430\u0434\u0438\u0439 \u0410\u0440\u0441\u0435\u043d\u0438\u0439
\u0410\u0440\u0442\u0451\u043c \u0410\u0440\u0442\u0443\u0440 \u0410\u0444\u0430\u043d\u0430\u0441\u0438\u0439
\u0411\u043e\u0433\u0434\u0430\u043d \u0411\u043e\u0440\u0438\u0441 \u0412\u0430\u0434\u0438\u043c
\u0412\u0430\u043b\u0435\u043d\u0442\u0438\u043d \u0412\u0430\u043b\u0435\u0440\u0438\u0439
\u0412\u0430\u0441\u0438\u043b\u0438\u0439 \u0412\u0435\u043d\u0438\u0430\u043c\u0438\u043d
\u0412\u0438\u043a\u0442\u043e\u0440 \u0412\u0438\u0442\u0430\u043b\u0438\u0439 \u0412\u043b\u0430\u0434
\u0412\u043b\u0430\u0434\u0438\u043c\u0438\u0440 \u0412\u043b\u0430\u0434\u0438\u0441\u043b\u0430\u0432
\u0412\u0441\u0435\u0432\u043e\u043b\u043e\u0434 \u0412\u044f\u0447\u0435\u0441\u043b\u0430\u0432
\u0413\u0430\u0432\u0440\u0438\u0438\u043b \u0413\u0430\u0440\u0440\u0438
\u0413\u0435\u043d\u043d\u0430\u0434\u0438\u0439 \u0413\u0435\u043e\u0440\u0433\u0438\u0439
\u0413\u0435\u0440\u0430\u0441\u0438\u043c \u0413\u0435\u0440\u043c\u0430\u043d \u0413\u043b\u0435\u0431
\u0413\u0440\u0438\u0433\u043e\u0440\u0438\u0439 \u0414\u0430\u0432\u0438\u0434
\u0414\u0430\u043d\u0438\u0438\u043b \u0414\u0435\u043d\u0438\u0441 \u0414\u043c\u0438\u0442\u0440\u0438\u0439
\u0415\u0432\u0433\u0435\u043d\u0438\u0439 \u0415\u0433\u043e\u0440 \u0415\u0444\u0438\u043c
\u0417\u0430\u0445\u0430\u0440 \u0418\u0432\u0430\u043d \u0418\u0433\u043d\u0430\u0442
\u0418\u0433\u043d\u0430\u0442\u0438\u0439 \u0418\u0433\u043e\u0440\u044c
\u0418\u043b\u043b\u0430\u0440\u0438\u043e\u043d \u0418\u043b\u044c\u044f
\u0418\u043c\u043c\u0430\u043d\u0443\u0438\u043b \u0418\u043e\u0441\u0438\u0444
\u041a\u0438\u0440\u0438\u043b\u043b \u041a\u043e\u043d\u0441\u0442\u0430\u043d\u0442\u0438\u043d
\u041b\u0435\u0432 \u041b\u0435\u043e\u043d\u0438\u0434 \u041c\u0430\u043a\u0430\u0440
\u041c\u0430\u043a\u0441\u0438\u043c \u041c\u0430\u0440\u0430\u0442 \u041c\u0430\u0440\u043a
\u041c\u0430\u0442\u0432\u0435\u0439 \u041c\u0438\u0445\u0430\u0438\u043b
\u041d\u0435\u0441\u0442\u043e\u0440 \u041d\u0438\u043a\u0438\u0442\u0430
\u041d\u0438\u043a\u043e\u043b\u0430\u0439 \u041e\u043b\u0435\u0433 \u041f\u0430\u0432\u0435\u043b
\u041f\u0451\u0442\u0440 \u0420\u043e\u0431\u0435\u0440\u0442
\u0420\u043e\u0434\u0438\u043e\u043d \u0420\u043e\u043c\u0430\u043d
\u0420\u043e\u0441\u0442\u0438\u0441\u043b\u0430\u0432 \u0420\u0443\u0441\u043b\u0430\u043d
\u0421\u0435\u043c\u0451\u043d \u0421\u0435\u0440\u0433\u0435\u0439 \u0421\u043f\u0430\u0440\u0442\u0430\u043a
\u0421\u0442\u0430\u043d\u0438\u0441\u043b\u0430\u0432 \u0421\u0442\u0435\u043f\u0430\u043d
\u0422\u0430\u0440\u0430\u0441 \u0422\u0438\u043c\u043e\u0444\u0435\u0439
\u0422\u0438\u043c\u0443\u0440 \u0422\u0440\u043e\u0444\u0438\u043c \u042d\u0434\u0443\u0430\u0440\u0434
\u042d\u0440\u0438\u043a \u042e\u043b\u0438\u0430\u043d \u042e\u0440\u0438\u0439
\u042f\u043a\u043e\u0432 \u042f\u0440\u043e\u0441\u043b\u0430\u0432 
\u0410\u043b\u0435\u043a\u0441\u0430\u043d\u0434\u0440\u0430 \u0410\u043b\u0438\u043d\u0430
\u0410\u043b\u0438\u0441\u0430 \u0410\u043b\u043b\u0430 \u0410\u043b\u0451\u043d\u0430
\u0410\u043b\u044c\u0431\u0438\u043d\u0430 \u0410\u043d\u0430\u0441\u0442\u0430\u0441\u0438\u044f
\u0410\u043d\u043d\u0430 \u0410\u043d\u0442\u043e\u043d\u0438\u043d\u0430
\u0410\u043d\u0436\u0435\u043b\u0438\u043a\u0430 \u0410\u043d\u0444\u0438\u0441\u0430
\u0412\u0435\u0440\u0430 \u0412\u0430\u043b\u0435\u0440\u0438\u044f \u0412\u0430\u0440\u0432\u0430\u0440\u0430
\u0412\u0430\u0441\u0438\u043b\u0438\u0441\u0430 \u0412\u043b\u0430\u0434\u043b\u0435\u043d\u0430
\u0412\u0435\u0440\u043e\u043d\u0438\u043a\u0430 \u0412\u0430\u043b\u0435\u043d\u0442\u0438\u043d\u0430
\u0412\u0438\u043a\u0442\u043e\u0440\u0438\u044f \u0413\u0430\u043b\u0438\u043d\u0430
\u0414\u0430\u0440\u044c\u044f \u0414\u0438\u043d\u0430 \u0414\u0438\u0430\u043d\u0430
\u0414\u043e\u043c\u0438\u043d\u0438\u043a\u0430 \u0415\u043a\u0430\u0442\u0435\u0440\u0438\u043d\u0430
\u0415\u043b\u0435\u043d\u0430 \u0415\u043b\u0438\u0437\u0430\u0432\u0435\u0442\u0430
\u0415\u0432\u0433\u0435\u043d\u0438\u044f \u0415\u0432\u0430 \u0416\u0430\u043d\u043d\u0430
\u0417\u0438\u043d\u0430\u0438\u0434\u0430 \u0417\u043e\u044f \u0417\u043b\u0430\u0442\u0430
\u0418\u043d\u0433\u0430 \u0418\u043d\u043d\u0430 \u0418\u0440\u0438\u043d\u0430
\u0418\u043d\u0435\u0441\u0441\u0430 \u0418\u0437\u0430\u0431\u0435\u043b\u043b\u0430
\u0418\u0437\u043e\u043b\u044c\u0434\u0430 \u0418\u0441\u043a\u0440\u0430 \u041a\u043b\u0430\u0440\u0430
\u041a\u043b\u0430\u0432\u0434\u0438\u044f \u041a\u0441\u0435\u043d\u0438\u044f
\u041a\u0430\u043f\u0438\u0442\u043e\u043b\u0438\u043d\u0430
\u041a\u043b\u0435\u043c\u0435\u043d\u0442\u0438\u043d\u0430
\u041a\u0440\u0438\u0441\u0442\u0438\u043d\u0430 \u041b\u0430\u0434\u0430
\u041b\u0430\u0440\u0438\u0441\u0430 \u041b\u0438\u0434\u0438\u044f \u041b\u044e\u0431\u043e\u0432\u044c
\u041b\u0438\u043b\u0438\u044f \u041b\u044e\u0434\u043c\u0438\u043b\u0430
\u041b\u044e\u0441\u044f \u041c\u0430\u0440\u0433\u0430\u0440\u0438\u0442\u0430
\u041c\u0430\u0439\u044f \u041c\u0430\u043b\u044c\u0432\u0438\u043d\u0430 \u041c\u0430\u0440\u0442\u0430
\u041c\u0430\u0440\u0438\u043d\u0430 \u041c\u0430\u0440\u0438\u044f \u041d\u0430\u0434\u0435\u0436\u0434\u0430
\u041d\u0430\u0442\u0430\u043b\u044c\u044f \u041d\u0435\u043b\u043b\u0438 \u041d\u0438\u043d\u0430
\u041d\u0438\u043a\u0430 \u041d\u043e\u043d\u043d\u0430 \u041e\u043a\u0441\u0430\u043d\u0430
\u041e\u043b\u044c\u0433\u0430 \u041e\u043b\u0435\u0441\u044f \u041f\u043e\u043b\u0438\u043d\u0430
\u0420\u0430\u0438\u0441\u0430 \u0420\u0430\u0434\u0430 \u0420\u043e\u0437\u0430\u043b\u0438\u043d\u0430
\u0420\u0435\u0433\u0438\u043d\u0430 \u0420\u0435\u043d\u0430\u0442\u0430
\u0421\u0432\u0435\u0442\u043b\u0430\u043d\u0430 \u0421\u043e\u0444\u044c\u044f \u0421\u043e\u0444\u0438\u044f
\u0422\u0430\u0438\u0441\u0438\u044f \u0422\u0430\u043c\u0430\u0440\u0430
\u0422\u0430\u0442\u044c\u044f\u043d\u0430 \u0423\u043b\u044c\u044f\u043d\u0430
\u0424\u0430\u0438\u043d\u0430 \u0424\u0435\u0434\u043e\u0441\u044c\u044f
\u0424\u043b\u043e\u0440\u0435\u043d\u0442\u0438\u043d\u0430 \u042d\u043b\u044c\u0432\u0438\u0440\u0430
\u042d\u043c\u0438\u043b\u0438\u044f \u042d\u043c\u043c\u0430 \u042e\u043b\u0438\u044f
\u042f\u0440\u043e\u0441\u043b\u0430\u0432\u0430 \u042f\u043d\u0430

Rene\u2019e A\u2019Laysyn, D\u2019Kota \u2019Ese Cam\u2019Ron Da\u2019neyelle
No\u2019elle ZI\u2019eyekel Miche\u2019le
""".strip())

first_names = first_names_female + first_names_male
names = first_names + last_names


# via: http://www.lipsum.com/feed/html
# russian is from: http://masterrussian.com/vocabulary/most_common_words.htm
# japanese (4bytes) are from: http://www.i18nguy.com/unicode/supplementary-test.html
ascii_paragraphs = '''
Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Phasellus
pharetra urna sit amet magna. Donec posuere porta velit. Vestibulum sed libero.
Ut vestibulum sodales arcu. Proin vulputate, mi quis luctus ornare, elit ligula fringilla nisi,
eu tempor purus felis a enim. Phasellus in justo et nisi rhoncus porttitor. Donec ligula felis,
sagittis at, vestibulum eu, vehicula sed, nisl. Aenean convallis pharetra nisl. Mauris imperdiet
libero eu urna ultrices vulputate. Donec semper nunc et nibh. In hac habitasse platea dictumst.
Fusce et ipsum semper velit tempor pharetra. Donec pretium sollicitudin purus. Cras mi velit,
egestas id, ultrices vitae, viverra sit amet, justo.

Quisque cursus tristique nunc. Fusce varius, orci et pellentesque aliquet,
nibh ipsum sodales lorem, iaculis tincidunt massa metus ut erat. Fusce dictum,
dolor ut laoreet aliquam, massa urna placerat nibh, vitae tristique nisl neque posuere mi.
Aliquam at orci. Nulla sem. Nullam risus. Nullam pharetra dapibus mauris. Mauris mollis pretium arcu.
Vestibulum sem massa, tempor a, dictum id, rutrum eu, ligula. Class aptent taciti sociosqu ad
litora torquent per conubia nostra, per inceptos himenaeos. Curabitur ultrices dignissim nibh.
Aenean nisl.

Integer bibendum pharetra orci. Suspendisse commodo, lorem elementum egestas hendrerit,
metus elit rutrum sapien, quis aliquam nibh nisi at ligula. Nam lobortis commodo mauris.
Vivamus semper, leo vel accumsan mattis, nulla elit vestibulum augue, vitae pharetra dolor nibh
sit amet odio. Pellentesque scelerisque ipsum id elit. Nulla aliquet semper dolor. Praesent ut lorem.
Curabitur dictum, magna eu porttitor rutrum, ipsum justo porttitor erat, sit amet tristique est ante
ut elit. Mauris vel est. In cursus, velit quis pharetra adipiscing, purus quam sagittis mi,
eget molestie leo lectus ac lacus. Curabitur ante massa, aliquam ut, scelerisque a, condimentum at,
eros. Nunc vitae neque. Nam sagittis scelerisque magna. Class aptent taciti sociosqu ad litora
torquent per conubia nostra, per inceptos himenaeos. Donec cursus pede. Quisque a mauris nec
turpis convallis scelerisque. Donec quam lorem, mollis vestibulum, euismod in, hendrerit et, sapien.
Curabitur felis.

Morbi pretium lorem imperdiet dui. Maecenas quis ligula. Morbi tempor velit sit amet felis.
Donec at dui. Donec neque. Quisque quis mauris a libero ultrices iaculis. Integer congue feugiat justo.
Quisque imperdiet lectus eu orci. Class aptent taciti sociosqu ad litora torquent per conubia nostra,
per inceptos himenaeos. Vivamus id lectus. Phasellus odio nisi, auctor eu, hendrerit quis,
iaculis sit amet, felis. Sed blandit mollis nunc. Sed velit magna, tristique tristique, porttitor ut,
dictum a, arcu. In hac habitasse platea dictumst. Cras semper bibendum tortor. Cum sociis natoque
penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse potenti.
In hac habitasse platea dictumst. Fusce mi sem, varius vitae, molestie ut, gravida venenatis, nibh.
Nam risus lectus, interdum at, condimentum eu, aliquet et, ipsum.

Mauris mi tortor, elementum ut, mattis eget, aliquam a, tellus.
Suspendisse porttitor orci. Donec rutrum diam non est. Duis ac nunc. Cras sollicitudin aliquet mi.
Cras in pede. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae;
Nam vehicula est at metus. Suspendisse sapien. Nunc lobortis tortor sed purus hendrerit pellentesque.
Nunc laoreet. Morbi pharetra. Integer cursus molestie turpis. Nam cursus sodales sem.
Maecenas non lacus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames
ac turpis egestas. Nam vel nibh eu nulla blandit facilisis. Sed varius turpis ac neque.
Curabitur vel erat. Morbi sed purus id erat tincidunt ullamcorper.
'''


unicode_paragraphs = '''
\u0437\u043d\u0430\u0442\u044c \u043c\u043e\u0439 \u0434\u043e \u0438\u043b\u0438 \u0435\u0441\u043b\u0438
\u0432\u0440\u0435\u043c\u044f \u0440\u0443\u043a\u0430 \u043d\u0435\u0442 \u0441\u0430\u043c\u044b\u0439
\u043d\u0438 \u0441\u0442\u0430\u0442\u044c \u0431\u043e\u043b\u044c\u0448\u043e\u0439 \u0434\u0430\u0436\u0435
\u0434\u0440\u0443\u0433\u043e\u0439 \u043d\u0430\u0448 \u0441\u0432\u043e\u0439 \u043d\u0443 \u043f\u043e\u0434
\u0433\u0434\u0435 \u0434\u0435\u043b\u043e \u0435\u0441\u0442\u044c \u0441\u0430\u043c \u0440\u0430\u0437
\u0447\u0442\u043e\u0431\u044b \u0434\u0432\u0430 \u0442\u0430\u043c \u0447\u0435\u043c \u0433\u043b\u0430\u0437
\u0436\u0438\u0437\u043d\u044c \u043f\u0435\u0440\u0432\u044b\u0439 \u0434\u0435\u043d\u044c \u0442\u0443\u0442
\u0432\u043e \u043d\u0438\u0447\u0442\u043e \u043f\u043e\u0442\u043e\u043c \u043e\u0447\u0435\u043d\u044c
\u0441\u043e \u0445\u043e\u0442\u0435\u0442\u044c \u043b\u0438 \u043f\u0440\u0438 \u0433\u043e\u043b\u043e\u0432\u0430
\u043d\u0430\u0434\u043e \u0431\u0435\u0437 \u0432\u0438\u0434\u0435\u0442\u044c \u0438\u0434\u0442\u0438
\u0442\u0435\u043f\u0435\u0440\u044c \u0442\u043e\u0436\u0435 \u0441\u0442\u043e\u044f\u0442\u044c
\u0434\u0440\u0443\u0433 \u0434\u043e\u043c \u0441\u0435\u0439\u0447\u0430\u0441 \u043c\u043e\u0436\u043d\u043e
\u043f\u043e\u0441\u043b\u0435 \u0441\u043b\u043e\u0432\u043e \u0437\u0434\u0435\u0441\u044c
\u0434\u0443\u043c\u0430\u0442\u044c \u043c\u0435\u0441\u0442\u043e \u0441\u043f\u0440\u043e\u0441\u0438\u0442\u044c
\u0447\u0435\u0440\u0435\u0437 \u043b\u0438\u0446\u043e \u0447\u0442\u043e \u0442\u043e\u0433\u0434\u0430
\u0432\u0435\u0434\u044c \u0445\u043e\u0440\u043e\u0448\u0438\u0439 \u043a\u0430\u0436\u0434\u044b\u0439
\u043d\u043e\u0432\u044b\u0439 \u0436\u0438\u0442\u044c \u0434\u043e\u043b\u0436\u043d\u044b\u0439
\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u043f\u043e\u0447\u0435\u043c\u0443
\u043f\u043e\u0442\u043e\u043c\u0443 \u0441\u0442\u043e\u0440\u043e\u043d\u0430 \u043f\u0440\u043e\u0441\u0442\u043e
\u043d\u043e\u0433\u0430 \u0441\u0438\u0434\u0435\u0442\u044c \u043f\u043e\u043d\u044f\u0442\u044c
\u0438\u043c\u0435\u0442\u044c \u043a\u043e\u043d\u0435\u0447\u043d\u044b\u0439 \u0434\u0435\u043b\u0430\u0442\u044c
\u0432\u0434\u0440\u0443\u0433 \u043d\u0430\u0434 \u0432\u0437\u044f\u0442\u044c \u043d\u0438\u043a\u0442\u043e
\u0441\u0434\u0435\u043b\u0430\u0442\u044c \u0434\u0432\u0435\u0440\u044c \u043f\u0435\u0440\u0435\u0434
\u043d\u0443\u0436\u043d\u044b\u0439 \u043f\u043e\u043d\u0438\u043c\u0430\u0442\u044c
\u043a\u0430\u0437\u0430\u0442\u044c\u0441\u044f \u0440\u0430\u0431\u043e\u0442\u0430 \u0442\u0440\u0438
\u0432\u0430\u0448 \u0443\u0436 \u0437\u0435\u043c\u043b\u044f \u043a\u043e\u043d\u0435\u0446
\u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0447\u0430\u0441 \u0433\u043e\u043b\u043e\u0441
\u0433\u043e\u0440\u043e\u0434 \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0439 \u043f\u043e\u043a\u0430
\u0445\u043e\u0440\u043e\u0448\u043e \u0434\u0430\u0432\u0430\u0442\u044c \u0432\u043e\u0434\u0430
\u0431\u043e\u043b\u0435\u0435 \u0445\u043e\u0442\u044f \u0432\u0441\u0435\u0433\u0434\u0430
\u0432\u0442\u043e\u0440\u043e\u0439 \u043a\u0443\u0434\u0430 \u043f\u043e\u0439\u0442\u0438
\u0441\u0442\u043e\u043b \u0440\u0435\u0431\u0451\u043d\u043e\u043a \u0443\u0432\u0438\u0434\u0435\u0442\u044c
\u0441\u0438\u043b\u0430 \u043e\u0442\u0435\u0446 \u0436\u0435\u043d\u0449\u0438\u043d\u0430
\u043c\u0430\u0448\u0438\u043d\u0430 \u0441\u043b\u0443\u0447\u0430\u0439 \u043d\u043e\u0447\u044c
\u0441\u0440\u0430\u0437\u0443 \u043c\u0438\u0440 \u0441\u043e\u0432\u0441\u0435\u043c
\u043e\u0441\u0442\u0430\u0442\u044c\u0441\u044f \u043e\u0431 \u0432\u0438\u0434 \u0432\u044b\u0439\u0442\u0438
\u0434\u0430\u0442\u044c \u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c \u043b\u044e\u0431\u0438\u0442\u044c
\u0441\u0442\u0430\u0440\u044b\u0439 \u043f\u043e\u0447\u0442\u0438 \u0440\u044f\u0434
\u043e\u043a\u0430\u0437\u0430\u0442\u044c\u0441\u044f \u043d\u0430\u0447\u0430\u043b\u043e
\u0442\u0432\u043e\u0439 \u0432\u043e\u043f\u0440\u043e\u0441 \u043c\u043d\u043e\u0433\u043e
\u0432\u043e\u0439\u043d\u0430 \u0441\u043d\u043e\u0432\u0430 \u043e\u0442\u0432\u0435\u0442\u0438\u0442\u044c
\u043c\u0435\u0436\u0434\u0443 \u043f\u043e\u0434\u0443\u043c\u0430\u0442\u044c \u043e\u043f\u044f\u0442\u044c
\u0431\u0435\u043b\u044b\u0439 \u0434\u0435\u043d\u044c\u0433\u0438 \u0437\u043d\u0430\u0447\u0438\u0442\u044c
\u043f\u0440\u043e \u043b\u0438\u0448\u044c \u043c\u0438\u043d\u0443\u0442\u0430 \u0436\u0435\u043d\u0430
'''


# only add 4-byte unicode if 4-byte unicode is supported
if sys.maxunicode > 65535:
    unicode_paragraphs += '''
\U0002070e \U00020731 \U00020779 \U00020c53 \U00020c78 \U00020c96 \U00020ccf \U00020cd5 \U00020d15 \U00020d7c
\U00020d7f \U00020e0e \U00020e0f \U00020e77 \U00020e9d \U00020ea2 \U00020ed7 \U00020ef9 \U00020efa \U00020f2d
\U00020f2e \U00020f4c \U00020fb4 \U00020fbc \U00020fea \U0002105c \U0002106f \U00021075 \U00021076 \U0002107b
\U000210c1 \U000210c9 \U000211d9 \U000220c7 \U000227b5 \U00022ad5 \U00022b43 \U00022bca \U00022c51 \U00022c55
\U00022cc2 \U00022d08 \U00022d4c \U00022d67 \U00022eb3 \U00023cb7 \U000244d3 \U00024db8 \U00024dea \U0002512b
\U00026258 \U000267cc \U000269f2 \U000269fa \U00027a3e \U0002815d \U00028207 \U000282e2 \U00028cca \U00028ccd
\U00028cd2 \U00029d98
'''


ascii_words = re.split(r'\s+', ascii_paragraphs.strip())
unicode_words = re.split(r'\s+', unicode_paragraphs.strip())
words_str = ascii_words + unicode_words


