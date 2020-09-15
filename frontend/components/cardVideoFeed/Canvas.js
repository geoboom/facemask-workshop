/* eslint-disable camelcase */
import React, { useEffect, useRef } from 'react';

const validDetections = (detectionsData) =>
  detectionsData &&
  detectionsData.results &&
  Array.isArray(detectionsData.results);

// given coords of bounding box, draws labelled bounding box around face
const drawBoundingBox = (ctx, coords, label, mask) => {
  ctx.font = 'bold 20px Arial';
  ctx.fillStyle = mask ? 'orange' : 'red';
  ctx.fillText(label, coords[0], coords[1] - 10);

  ctx.beginPath();
  ctx.lineWidth = '2';
  ctx.strokeStyle = mask ? 'orange' : 'red';
  ctx.rect(...coords);
  ctx.stroke();
};

// this is the canvas component that draws bounding box over face
const Canvas = ({ videoMetadata, detectionsData }) => {
  const canvasRef = useRef(null);

  // this clears and redraws the bounding box on the canvas
  // if the bounding box coords change
  useEffect(() => {
    if (canvasRef != null) {
      // get the context of html canvas element's ref
      const canvas = canvasRef.current;
      const ctx = canvas.getContext('2d');

      // clear the previous bounding box
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      // don't proceed further if our detectionsData is not well-formed
      if (!validDetections(detectionsData)) return;

      // for each detection we have, draw the corresponding bounding box
      // around the face which has been detected
      detectionsData.results.forEach(({ wearing_mask, confidence, coords }) => {
        const label = `${wearing_mask ? 'MASK' : 'NO MASK'} ${(
          100 * confidence
        ).toFixed(1)}%`;

        try {
          drawBoundingBox(ctx, coords, label, wearing_mask);
        } catch (e) {
          console.log('error drawing bounding box:', e);
        }
      });
    }
  }, [detectionsData.flag]);

  // this forces canvas dimensions to be the same as video dimensions
  useEffect(() => {
    if (canvasRef != null) {
      const canvas = canvasRef.current;

      // ensures canvas has same aspect ratio as video
      canvas.height =
        (canvas.width * videoMetadata.height) / videoMetadata.width;
    }
  }, [videoMetadata.height, videoMetadata.width]);

  return <canvas ref={canvasRef} />;
};

export default Canvas;
