import React, { useEffect, useState } from 'react';
import Head from 'next/head';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

import styles from '../styles/Home.module.scss';
import CardVideoFeed from '../components/cardVideoFeed/CardVideoFeed';
import CardDetectionLog from '../components/cardDetectionLog/CardDetectionLog';
import FooterContent from '../components/footerContent/FooterContent';
import detector from '../utils/detector';
import { LOOP_INTERVAL_MS } from '../config';

const Home = () => {
  const [imageUrls, setImageUrls] = useState([]);
  const [detectionsData, setDetectionsData] = useState({
    flag: true,
    detections: [],
  });

  const updateImageUrls = () => {
    detector.updateDetectionLog(setImageUrls);
  };

  // fetch all our detection pic urls when the app first loads
  useEffect(() => {
    updateImageUrls();
  }, []);

  const startDetectionLoop = (video) => {
    detector.createImageContext(document);

    // every interval send a frame/snapshot of the video feed for detection
    return setInterval(() => {
      detector.detectFaceMask(video).then((data) => {
        // retrieve all the picture urls in detection log if it was updated
        if (data.detection_log_updated) {
          updateImageUrls();
        }

        // update our detections data
        setDetectionsData((prev) => ({
          flag: !prev.flag,
          results: data.results,
          logs: data.logs,
        }));
      });
    }, LOOP_INTERVAL_MS);
  };

  return (
    <div className={styles.container}>
      <Head>
        <title>Facemask Detector 9k</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <header className={styles.header}>
        <h2>Facemask Detector 9k</h2>
      </header>

      <main className={styles.main}>
        <Container fluid>
          <Row>
            <Col xs={12} md={6} lg={5} xl={4}>
              <CardVideoFeed
                startDetectionLoop={startDetectionLoop}
                detectionsData={detectionsData}
              />
            </Col>
            <Col xs={12} md={6} lg={7} xl={8} className="mt-3 mt-md-0">
              <CardDetectionLog imageUrls={imageUrls} />
            </Col>
          </Row>
        </Container>
      </main>

      <footer className={styles.footer}>
        <FooterContent />
      </footer>
    </div>
  );
};

export default Home;
