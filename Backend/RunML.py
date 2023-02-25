from transformers import pipeline

def oneLineSummary(abstract: str) -> str:
    summarizer = pipeline("text2text-generation", model='snrspeaks/t5-one-line-summary')
    return summarizer(abstract)

def researchPaperSummary(paper: str) -> str:
    summarizer = pipeline("summarization", model='pszemraj/led-base-book-summary')
    return summarizer(paper)

def getCategories(abstract: str):
    summarizer = pipeline("zero-shot-classification", model='valhalla/distilbart-mnli-12-1')
    categories = ['Self Driving', 'Transport', 'Simulation', '3D Model']
    results = summarizer(abstract, categories)
    return results['labels'], results['scores']

def test_oneLineSummary():
    text = """Bluetooth Low Energy (BLE) has become the de facto communication protocol for the
    Internet of Things (IoT) and smart wearable devices for its ultra-low energy consumption, ease of
    development, good enough network coverage, and data transfer speed. Due to the simplified design of
    this protocol, there have been lots of security and privacy vulnerabilities. As billions of health care, personal
    fitness wearable, smart lock, industrial automation devices adopt this technology for communication, its
    vulnerabilities should be dealt with high priority. Some segregated works on BLE were performed focusing
    on various vulnerabilities, such as the insecure implementation of encryption, device authentication, user
    privacy, etc. However, there has been no comprehensive survey on the security vulnerabilities of this
    protocol. In this survey paper, we present a comprehensive taxonomy for the security and privacy issues
    of BLE. We present possible attack scenarios for different types of vulnerabilities, classify them according
    to their severity, and list possible mitigation techniques. We also provide case studies regarding how
    different vulnerabilities can be exploited in real BLE devices."""

    print(oneLineSummary(text))

def test_researchPaperSummary():
    text = """Predicting a human drivers lane-changing behaviour is a fundamental step for self-driving vehicles. It can also be used in Advanced Driver Assistance Systems (ADAS), Accident Prevention, and Regulation. Over the years, researchers have developed various techniques to achieve this objective, including the use of Back Propagating Neural Networks (BPNNs) and Recurrent Neural Networks (RNNs). The Next Generation Simulation (NGSIM) dataset, developed by the US Department of Transportation, provides the positional data for 4 highways across the US and is the basis for this project. The goal of this project is to produce a 3D simulation package in python that can be used by researchers to observe and validate the performance of their models
    To achieve this goal, the project was split into 2 tracks. The first track was focused on developing the simulating algorithm while trying to minimize the number of collisions that take place between vehicles. While the 2nd track focused on creating beautiful 3D models of vehicles (using the vpython package) that can be scaled according to the data. These 2 tracks were then merged to create the final model with the average collisions per frame being minimized to 70, 110, and 45 for the i80, us-101, and Peachtree highways respectively.
    Keywords - Autonomous Vehicles, NGSIM, 3D Simulation
    1 INTRODUCTION
    Lane changing has a significant effect on traffic flow. When done incorrectly it can lead to traffic congestion and accidents. Hence, predicting the lane changing behaviour of human driver’s is a fundamental step for self-driving vehicles. It is a highly researched topic with applications that include Advanced Driver Assistance Systems (ADAS), accident prevention and regulation.
    There are two types of lane changes that usually occur on roads: Mandatory Lane changes and Discretionary Lane changes. Mandatory lanes changes are those that usually take place near an intersection or a highway exit where the driver changes their lane in anticipation of an upcoming turn. This could also take place at a diversion when the driver’s current lane is closed downstream. Discretionary Lane changes, on the other hand, usually take place on long straight sections of highway where the driver desires a different speed, line of sight, ride quality, etc. from the current lane. Due the different driver motives, Discretionary and Mandatory Lane changes should be considered separately. For example, distance between the subject vehicle and surrounding vehicles has a larger impact on driver decisions while they perform discretionary lane changes as compared to mandatory lane changes [1]. Since it is difficult to predict mandatory lane changes without information about the driver’s destination, the scope of this paper will be confined to discretionary lanes changes.
    Traditional Lane changing models try to predict the velocity, acceleration and position of the subject vehicle as a function of the distance between lanes, the time when the vehicle successfully adjusts for lateral acceleration, the time when the subject vehicle arrives at the marginal collision point, and the time when the subject vehicle finishes lateral acceleration [2]. These models are generally aimed at predicting how a lane change that has already began will proceed but cannot consider the uncertainties in human behaviour [3]. They are therefore ineffective in predicting the time at which a lane change will take place.
    To solve this problem researchers are trying to use different types of artificial neural networks (ANNs). Artificial Neural Networks consist of an input layer, various hidden layers and an output layer, with each node mimicking the neuron in the human brain. This is also referred to as Deep Learning. There are various types of artificial neural networks. Researchers have successfully been able to use Back Propagation Neural Networks (BPNNs) to predict the lane changing behaviour of human drivers [3]. Other researchers have also been able to use Recurrent Neural Networks like Elman Networks and Bayesian Inference LSTMs (Long Short Term Memory) for the same [4]. Recurrent Neural Networks can take time into account unlike regular Neural Networks. Long Short Term Memory (LSTMs) build on Recurrent Neural Networks to help them better consider time
    Proceedings of the URECA@NTU 2021-22
    series data without forgetting about old data to process new data (a common problem with Recurrent Neural Networks (RNNs)). With the recent advances in Transformer Neural Networks, the use of ANNs for lane change prediction will continue to be a hot topic for researchers.
    The Next Generation Simulation (NGSIM) Program was developed by the United States, Department of Transportation with the goal “To develop a core of open behavioural algorithms in support of traffic simulation with a primary focus on microscopic modelling, including supporting documentation and validation data sets that describe the interactions of multimodal travellers, vehicles and highway systems, and interactions presented to them from traffic control devices, delineation, congestion, and other features of the environment.” [5]. The Next Generation Simulation (NGSIM) Dataset contains vehicle trajectory data from the southbound US 101 and Lankershim Boulevard in Los Angeles, CA, eastbound I-80 in Emeryville, CA and Peachtree Street in Atlanta, Georgia. This was done through a network of video cameras, collecting video data which was then run through a software called NGVIDEO to get the final results. The dataset contains the precise location of every vehicle, relative to other vehicles, in the study area for each tenth of a second [6]. The NGSIM Dataset is the most popular public dataset for lane change prediction and will the base for this project as well.
    The goal of this project is to develop a comprehensive 3D Simulation package in python which can be used by researchers to observe and validate the performance of their models. This package will be built using the NGSIM Dataset as the data source.
    2 METHODOLOGY
    During development, this project was split into 2 tracks. The first track was focused on developing the simulating algorithm while trying to minimize the number of collisions that take place between vehicles. While the 2nd track was focused on creating beautiful 3D models of vehicles (using the vpython package) that can be scaled according to the data. These 2 tracks were then merged to create the 3D final model.
    2.1 SIMULATING ALGORITHM
    Data cleaning is an essential part of any research work. Different techniques of data cleaning can have a different and significant effects on the results. Hence, this project was designed to keep data cleaning at a minimum so that we don’t interfere with the work of our package’s users. The only data cleaning done in this project was separating the NGSIM Dataset into 4 separate datasets based on location. This was done in order to prevent the simulating algorithm from getting confused between data from different locations. The data used in the simulation remained limited to the columns: ‘Vehicle_ID’, ‘Frame_ID’, ‘Local_X’, ‘Local_Y’, ‘v_length’, ‘v_Width’, ‘v_Class’, ‘v_Vel’, and ‘v_Acc’. This helped reduce the amount of memory used by the simulation, a critical step since the simulation is quite memory hungry itself.
    The simulating algorithm runs through the NGSIM Dataset (for a single location) iteratively. It maintains a dictionary of all vehicles currently in the simulation containing their location, type, speed, and acceleration. For each frame the algorithm reads through the data and updates the positions of the vehicles in the dictionary, a new frame of the simulation is then rendered before moving on to the next frame in the data. The algorithm has been designed in such a way that the simulation renders 10 frames each second. The same frame rate as the cameras used for collecting the NGSIM Data [6]. However, there were some vehicles (identified by their unique Vehicle_ID) who were not present in a particular frame but were present in preceding and successive frames. In order to prevent vehicles from continuously disappearing and reappearing in the simulation, something had to be done to infer the position of the missing vehicle in that particular frame.
    Two approaches were used to deal with this problem: Vel_Const and Acc_Const. Vel_Const assumes that the velocity of a vehicle remains constant in the absence of any other information. Acc_Const assumes that the acceleration of a vehicle remains constant in the absence of any other information. The pseudo codes for both algorithms are given below.
    A cutoff was added to both algorithms. This prevents vehicles from crossing a certain threshold of Local_Y. This was done so that vehicles are not rendered after exiting the area of study. Further results of this cutoff will be explored in the ahead.
    Fig 1.1 : Pseudocode for Vel_Const
    Proceedings of the URECA@NTU 2021-22
    Fig 1.2: Pseudocode for Acc_Const
    2.2 TWO-DIMENSIONAL SIMULATION
    A two-dimensional (2D) simulation was created in order to test the above algorithms. This simulation was created using the Tkinter library in python. It depicts a bird eye view of the study area. Each automobile is depicted as a red rectangle with dimensions to scale with those in the NGSIM dataset. The simulation renders 10 frames a second, the same rate as that of the data capture for the NGSIM dataset. The two-dimensional simulation was a great tool for debugging and refining the above algorithms. It also has a much smaller computational overhead and memory use compared to the 3D simulation. Screenshots of the 2D simulation have been depicted in Fig 2.1 and Fig 2.2.
    Fig 2.1: Screenshot of 2D Simulation of i80
    2.3 3D MODELS OF VEHICLES
    The next step in creating a 3D simulation was designing 3D models for the vehicles. The final design was inspired by that of a simple matchbox car. Using such a design had quite a few benefits. The 1st benefit is that a matchbox design is easy to make yet instantly recognisable. This also reduced the overall computational overhead of the simulation which would have increased tremendously if a more detailed model had been used. The 2nd benefit of using a matchbox design was that its dimensions could be changed to match those in the NGSIM data without making the vehicle look ugly. Unlike the 2D simulation, v_Class (vehicle class) was taken into consideration here. Three separate 3D models were designed and built: one for Light Motor Vehicles (LMVs) resembling a car, one for two wheelers resembling a scooter, and one for heavy vehicles resembling a truck. Figures of these models are given below.
    Fig 3.1 : 3D Model for LMVs (Front View)
    Fig 3.2: 3D Model for LMVs (Rear View)
    Fig 3.3: 3D Model for Truck (Front View)
    Fig 2.2: Screenshot of 2D Simulation of us101
    Proceedings of the URECA@NTU 2021-22
    Fig 3.4: 3D Model for Truck (Rear View)
    Fig 3.5: 3D Model for Scooter (Front View)
    Fig 3.6: 3D Model for Scooter (Rear View)
    2.4 THE FINAL 3D SIMULATION
    The final 3D simulation was built using the simulating algorithm described in 2.1 and the 3D models in 2.3. The simulation was built using vpython, a simple library used to build 3D animations in python [7]. The simulation package allows users to be able to customise the colour of the vehicles in the simulation. All colours except red and white are allowed. (Since then the headlamps and taillamps would get camouflaged.) The package also gives the user the option to specify the cut-off mentioned in the algorithms in 2.1 (optional).
    Figs 4.1 & 4.2: Screenshot of simulation for i80
    3 RESULTS & DISCUSSION
    In order to measure the accuracy of the simulating algorithms, the number of collisions between vehicles was measured. Given below are the no of collisions between vehicles per frame in the NGSIM Dataset for the i80, us-101, and peachtree. Lankershim was not used as it contained an intersection and thus fell under the domain of mandatory lane changes instead of discretionary ones.
    Note: The no of collisions per frame data has been smoothened with a window size of 250 using a moving average.
    Proceedings of the URECA@NTU 2021-22
    Figs 5.1 to 5.4: No of Collisions per frame
    While Acc_Const has a lesser no of collisions per frame, it suffers from another problem. Some vehicles go in reverse after a sudden brake as their acceleration remains constant at a high negative value until new data comes. While the increase in the no of collisions caused by this is lesser than the amount reduced after switching from Vel_Const, it is a highly noticeable error. Both algorithms would be provided in the package with Acc_Const as the default so that researchers can choose the appropriate algorithm. Smoothening of the NGSIM data will reduce the no of collisions taking place. However, this was kept to a minimum as the goal is to develop a package that should not interfere with our user’s work.
    4 CONCLUSION
    This project develops a 3D simulation package in python based on the NGSIM Dataset. It is focused on enabling researchers to visualise the discretionary lane changing behaviour of human drivers and validate the performance of their models. The simulation provides 2 algorithms for use: Vel_Const and Acc_Const. Acc_Const has a lesser number of collisions between vehicles but suffers from the presence of reversing vehicles. The package has separate 3D Models for Light Motor Vehicles (LMVs), Heavy Vehicles, and Two Wheelers.
    ACKNOWLEDGMENT
    I would like to acknowledge the funding support from Nanyang Technological University URECA Undergraduate Research Programme for this research project.
    REFERENCES
    [1] M. Vechione, E. Balal, and R. L. Cheu, “Comparisons of mandatory and discretionary lane changing behavior on freeways,” International Journal of Transportation Science and Technology, 10-Mar-2018. [Online]. Available: https://www.sciencedirect.com/science/article/pii/S2046043017300886?via%3Dihub. [Accessed: 19-Jun-2022]. [2] Wang, W.H., Ding, C.X., Feng, G.D. and Jiang, X.B., 2010. Simulation modelling of longitudinal safety spacing in inter-vehicles dynamics interactions. Journal of Beijing Institute of Technology, 19(supplement 2), pp.55-60.
    [3] C. Ding, W. Wang, X. Wang, and M. Baumann, “A neural network model for driver's Lane-changing trajectory prediction in urban traffic flow,” Mathematical Problems in Engineering, 25-Feb-2013. [Online]. Available: https://doi.org/10.1155/2013/967358. [Accessed: 19-Jun-2022].
    [4] J. Wang, Z. Zhang, and G. Lu, “A bayesian inference based Adaptive Lane Change Prediction Model,” Transportation Research Part C: Emerging Technologies, 09-Sep-2021. [Online]. Available: https://www.sciencedirect.com/science/article/abs/pii/S0968090X2100365X?via%3Dihub. [Accessed: 19-Jun-2022].
    [5] The Federal Government of the United States, Department of Transportation, “Next
    Proceedings of the URECA@NTU 2021-22
    generation simulation (NGSIM),” Traffic Analysis Tools: Next Generation Simulation - FHWA Operations. [Online]. Available: https://ops.fhwa.dot.gov/trafficanalysistools/ngsim.htm. [Accessed: 19-Jun-2022].
    [6] The Federal Government of the United States, Department of Transportation, “Next generation simulation (NGSIM) vehicle trajectories and supporting data: Department of Transportation - Data Portal,” Data.Transportation.gov. [Online]. Available: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Vehicle-Trajector/8ect-6jqj/data. [Accessed: 19-Jun-2022].
    [7] B. Sherwood, VPython. [Online]. Available: https://vpython.org/. [Accessed: 22-Jun-2022]."""
    print(researchPaperSummary(text))

def test_getCategories():
    abstract = """Predicting a human drivers lane-changing behaviour is a fundamental step for self-driving vehicles. It can also be used in Advanced Driver Assistance Systems (ADAS), Accident Prevention, and Regulation. Over the years, researchers have developed various techniques to achieve this objective, including the use of Back Propagating Neural Networks (BPNNs) and Recurrent Neural Networks (RNNs). The Next Generation Simulation (NGSIM) dataset, developed by the US Department of Transportation, provides the positional data for 4 highways across the US and is the basis for this project. The goal of this project is to produce a 3D simulation package in python that can be used by researchers to observe and validate the performance of their models
    To achieve this goal, the project was split into 2 tracks. The first track was focused on developing the simulating algorithm while trying to minimize the number of collisions that take place between vehicles. While the 2nd track focused on creating beautiful 3D models of vehicles (using the vpython package) that can be scaled according to the data. These 2 tracks were then merged to create the final model with the average collisions per frame being minimized to 70, 110, and 45 for the i80, us-101, and Peachtree highways respectively."""
    print(getCategories(abstract))

test_getCategories()