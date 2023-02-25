from transformers import pipeline
import nltk

nltk.download('punkt')

def oneLineSummary(abstract: str) -> str:
    summarizer = pipeline("text2text-generation", model='snrspeaks/t5-one-line-summary')
    return summarizer(abstract)

def researchPaperSummary(paper: str) -> str:
    summarizer = pipeline("summarization", model='pszemraj/led-base-book-summary')
    return summarizer(paper)

def getCategoryWeights(abstract: str, categories: list):
    summarizer = pipeline("zero-shot-classification", model='valhalla/distilbart-mnli-12-1')
    results = summarizer(abstract, categories)
    return results['labels'], results['scores']

def getNouns(text: str):
    text = nltk.word_tokenize(text)
    results = nltk.pos_tag(text)
    noun_set = set([])
    for el in results:
        if(el[1] == 'NN' or el[1] == 'NNS' or el[1] == 'NNPS' or el[1] == 'NNP'):
            noun_set.add(el[0])
    return list(noun_set)


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
    """
    print(researchPaperSummary(text))

def test_getCategoryWeights():
    abstract = """Predicting a human drivers lane-changing behaviour is a fundamental step for self-driving vehicles. It can also be used in Advanced Driver Assistance Systems (ADAS), Accident Prevention, and Regulation. Over the years, researchers have developed various techniques to achieve this objective, including the use of Back Propagating Neural Networks (BPNNs) and Recurrent Neural Networks (RNNs). The Next Generation Simulation (NGSIM) dataset, developed by the US Department of Transportation, provides the positional data for 4 highways across the US and is the basis for this project. The goal of this project is to produce a 3D simulation package in python that can be used by researchers to observe and validate the performance of their models
    To achieve this goal, the project was split into 2 tracks. The first track was focused on developing the simulating algorithm while trying to minimize the number of collisions that take place between vehicles. While the 2nd track focused on creating beautiful 3D models of vehicles (using the vpython package) that can be scaled according to the data. These 2 tracks were then merged to create the final model with the average collisions per frame being minimized to 70, 110, and 45 for the i80, us-101, and Peachtree highways respectively."""
    print(getCategoryWeights(abstract))

def test_getNouns():
    text = """Predicting a human drivers lane-changing behaviour is a fundamental step for self-driving vehicles. It can also be used in Advanced Driver Assistance Systems (ADAS), Accident Prevention, and Regulation. Over the years, researchers have developed various techniques to achieve this objective, including the use of Back Propagating Neural Networks (BPNNs) and Recurrent Neural Networks (RNNs). The Next Generation Simulation (NGSIM) dataset, developed by the US Department of Transportation, provides the positional data for 4 highways across the US and is the basis for this project. The goal of this project is to produce a 3D simulation package in python that can be used by researchers to observe and validate the performance of their models
    To achieve this goal, the project was split into 2 tracks. The first track was focused on developing the simulating algorithm while trying to minimize the number of collisions that take place between vehicles. While the 2nd track focused on creating beautiful 3D models of vehicles (using the vpython package) that can be scaled according to the data. These 2 tracks were then merged to create the final model with the average collisions per frame being minimized to 70, 110, and 45 for the i80, us-101, and Peachtree highways respectively.
    """
    print(getNouns(text))
