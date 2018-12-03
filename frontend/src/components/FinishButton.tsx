import * as React from 'react';

export type FinishButtonType = {
  version: number;
};

const finishStyle = {
  marginTop: '10em'
};

export const FinishButton = (props: FinishButtonType) => {
  let link;
  if (props.version === 1) {
    link = 'https://docs.google.com/forms/d/e/1FAIpQLSfceznyF7-5EpkXlDHCWPgKEJ0Frrh4tTMBkR40rne-Lokang/viewform?usp=sf_link';
  }
  else if (props.version === 2) {
    link = 'https://docs.google.com/forms/d/e/1FAIpQLSfRAcQXT8Ke-G_oVVKDVucTCZMYajw9-v6bQ21fkq_sk9lzHA/viewform?usp=sf_link';
  }
  else if (props.version === 3) {
    link = 'https://docs.google.com/forms/d/e/1FAIpQLSeUyfve_K-Z-k6D1luC04mQXjJSsHmFEqGKy_hyzMjEivgG9g/viewform?usp=sf_link';
  }
  else {
    link = 'https://docs.google.com/forms/d/e/1FAIpQLSdMX-MvJAobHnjvM34huz_7ZXfAX4P_CPJJkqWExWWiggM_-w/viewform?usp=sf_link';
  }

  return (
    <a href={link} >
      <button type="button" className={`btn btn-lg btn-danger`} style={finishStyle}>
        Finish
      </button>
    </a>
  );
};
