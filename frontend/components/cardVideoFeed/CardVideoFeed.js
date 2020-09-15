import React, { useEffect, useState, useRef } from 'react';
import Card from 'react-bootstrap/Card';

import styles from '../../styles/CardVideoFeed.module.scss';
import Canvas from './Canvas';

const logs = [
  {
    text: 'Total detections',
    attr: 'detections',
    isTime: false,
  },
  {
    text: 'Latest detection',
    attr: 'latest_time',
    isTime: true,
  },
  {
    text: 'Average detection',
    attr: 'avg_time',
    isTime: true,
  },
];

const CardVideoFeed = ({ startDetectionLoop, detectionsData }) => {
  const [videoMetadata, setVideoMetadata] = useState({
    frameRate: '-',
    width: '-',
    height: '-',
  });
  const videoEl = useRef(null);

  // when this component loads, access the user's webcam
  useEffect(() => {
    let interval = null;

    // get user permission to use webcam
    navigator.mediaDevices
      .getUserMedia({
        video: { facingMode: 'user' }, // front camera on mobile
        audio: false,
      })
      .then((stream) => {
        // permission granted
        // here, "stream" refers to the webcam video

        // a reference to the html video element (<video />)
        const video = videoEl.current;

        // set the element's source to our webcam stream and play!
        video.srcObject = stream;
        video.play();

        setVideoMetadata(stream.getTracks()[0].getSettings());

        // pass our video feed into the detection loop for detection
        interval = startDetectionLoop(video);
      });

    // cleanup
    return () => clearInterval(interval);
  }, []);

  const Details = () =>
    logs.map(({ text, attr, isTime }) => (
      <>
        <br />
        <strong>{text}</strong>
        {': '}
        {detectionsData && detectionsData.logs && detectionsData.logs[attr]
          ? isTime && parseFloat(detectionsData.logs[attr])
            ? `${detectionsData.logs[attr].toFixed(3)}s`
            : detectionsData.logs[attr]
          : '-'}
      </>
    ));

  return (
    <Card>
      <div className={styles.videoContainer}>
        <Canvas detectionsData={detectionsData} videoMetadata={videoMetadata} />
        {/* eslint-disable-next-line jsx-a11y/media-has-caption */}
        <video ref={videoEl} autoPlay />
      </div>
      <Card.Body>
        <Card.Title>Live Feed</Card.Title>
        <Card.Text>
          <strong>Data:</strong> {videoMetadata.frameRate} fps,{' '}
          {videoMetadata.width} * {videoMetadata.height},{' '}
          {(videoMetadata.width / videoMetadata.height).toFixed(3)}
          <Details />
        </Card.Text>
      </Card.Body>
    </Card>
  );
};

export default CardVideoFeed;
