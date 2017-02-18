import config
import trainer

def main():
    cfg = config.Config(filename_queue="dataset/flowers.tfrecords")
    t = trainer.Trainer(cfg)
    t.fit()

if __name__ == "__main__":
    main()
