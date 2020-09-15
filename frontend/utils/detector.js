import { API_URL } from '../config';

const UPLOAD_WIDTH = 300;

let imageCanvas;
let imageCtx;

const createImageContext = (document) => {
  imageCanvas = document.createElement('canvas');
  imageCanvas.width = UPLOAD_WIDTH;

  imageCtx = imageCanvas.getContext('2d');
};

const detectFaceMask = async (video) => {
  const { videoWidth, videoHeight } = video;

  imageCanvas.height = UPLOAD_WIDTH * (videoHeight / videoWidth);

  imageCtx.drawImage(
    video,
    0,
    0,
    videoWidth,
    videoHeight,
    0,
    0,
    UPLOAD_WIDTH,
    UPLOAD_WIDTH * (videoHeight / videoWidth),
  );

  let data = {};

  const file = await new Promise((resolve) =>
    imageCanvas.toBlob(resolve, 'image/jpeg'),
  );

  const formData = new FormData();
  formData.append('file', file);

  try {
    const res = await fetch(`${API_URL}/detect`, {
      method: 'POST',
      body: formData,
    });
    data = await res.json();
  } catch (err) {
    console.error('detectFaceMask upload error:', err);
  }

  return data;
};

const updateDetectionLog = (cb) => {
  fetch(`${API_URL}/detection_log`)
    .then((res) => res.json())
    .then((data) => {
      cb(data.map((filename) => `${API_URL}/detection_log/${filename}`));
    })
    .catch((err) => {
      console.log('updateDetectionLog error', err);
    });
};

export default {
  createImageContext,
  detectFaceMask,
  updateDetectionLog,
};
