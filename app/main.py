import monteCarloAlgo
import logging
import whisperWorkload

def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Starting program")
    
     # Number of random points to generate
    num_points = 1

    # Estimating pi
    pi_approximation = monteCarloAlgo.estimate_pi(num_points)
    print("Approximation of pi using Monte Carlo method:", pi_approximation[0])
    logObjcets = pi_approximation[1]
    for obj in logObjcets:
        logging.info(obj)

    whisperResult = whisperWorkload.loadModel()
    logging.info("Now starting Whisper workload")
    for obj in whisperResult[0]:
        print(obj)
        for info in whisperResult[1]:
            logging.info(info)



if __name__ == "__main__":
    main()
    
    