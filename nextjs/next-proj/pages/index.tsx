import Head from 'next/head'
import { Poppins } from 'next/font/google'
import styles from '@/styles/Home.module.css'
import { NextPageContext } from 'next';

const poppins = Poppins({ weight: ['700'], subsets: ['latin-ext'] })

export default function Home() {
  const handleButtonClick = () => {
    window.location.href = 'https://github.com/de-y/';
  };

  return (
    <>
      <Head>
        <title>de-y's Page</title>
        <meta name="description" content="Generated by create next app" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main>
        <br />
        <h1 className="text-4xl md:text-5xl lg:text-6xl font-bold font-display text-center">
          <strong>de-y.</strong>
        </h1>
        <br /><br /><br /><br /><br />
        <div className={styles.main}>
          <h1 className="text-4xl md:text-8xl lg:text-9xl font-bold font-display">
            Learning how to build{' '}
            <h1 className="text-4xl md:text-8xl lg:text-9xl font-bold font-display underline">
              better
            </h1>{' '}
            applications.
            <br />One step at a time.
          </h1>
          <button  className="bg-blue-500 hover:bg-blue-700 text-white py-4 px-8 rounded-full mt-4 md:mt-8 lg:mt-12" style={{ marginTop: '1rem' }} onClick={handleButtonClick}>Visit GitHub Profile</button>
        </div>

        <div className={styles.footer}>
          <br />
          <h1 className="text-2xl md:text-3xl lg:text-4xl font-bold font-display text-center">
            de-y.
          </h1>
          <br />
          <h1 className="text-base md:text-xl lg:text-1xl font-display text-center">
            Website written in JSX and uses NextJS as the tech stack and tailwind
            for CSS.
            <br />
            <br />©2023 de-y. All rights reserved.
          </h1>
        </div>
      </main>
    </>
  )
}
