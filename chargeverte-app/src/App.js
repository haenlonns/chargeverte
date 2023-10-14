import React from 'react'; 
import './App.css'; 
import graph from './images/co2 emissions by time crop.png';
import bar from './images/bar.png';

import Stack from 'stack-styled';
import styled, { ThemeProvider, createGlobalStyle } from 'styled-components'
import {
  fontSize,
  fontWeight,
  lineHeight,
  marginRight,
} from 'styled-system'
import { width, height, space, color } from 'styled-system';

const Box = styled('div')(
	{
		boxSizing: 'border-box',
	},
	width,
	height,
	space,
	color
);


const Text = styled.div`
  ${space}
  ${fontSize}
  ${fontWeight}
  ${lineHeight}
  ${color}
`
Text.propTypes = {
  ...space.propTypes,
  ...fontSize.propTypes,
  ...fontWeight.propTypes,
  ...lineHeight.propTypes,
  ...color.propTypes,
}
const Image = styled.img`
	max-width: 100%;
  margin-left: auto;
  margin-right:auto;
`;

const Para = styled.p`
	margin-top: 0;
	margin-bottom: 16px;
  margin-right: 5%;
  margin-left: 5%;
	line-height: 1.5;
	font-size: 1.2rem;
	font-family: Georgia, 'Times New Roman', Times, serif;
`;
const Heading = styled.h1`
	margin-top: 16px;
	margin-bottom: 32px;
	line-height: 1.1;
	font-weight: normal;
	font-size: 1.5rem;
	font-family: Georgia, 'Times New Roman', Times, serif;
  text-align: center;
`;





function App() { 
	return ( 
		<Stack
      gridGap={10}
      gridTemplateColumns="100%"
>

      <Stack gridColumn="">
        <div> 
            <nav class="navbar light_green"> 
            <h1 class="text-big"> 
              ChargeVerte
            </h1> 
            </nav> 
          </div>
        <Image src={graph} alt="graph" />
        <Heading>Find your optimal charging time</Heading>
        <Para>
          What is your charging interval?
        </Para>
        <Para>
          How many hours do you need to charge for?
        </Para>
        <Para>
          To minimise carbon output, you should start charging at:
        </Para>

      </Stack>
    </Stack>
  ) 
} 

export default App 
