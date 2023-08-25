import styled from "styled-components";

export const Wrapper = styled.div`
  max-width: 1920px;
  max-height: 1080px;
  width: 100%;
  height: 100vh;
  position: relative;
`;
export const Logo = styled.div`
  width: 130px;
  height: 130px;
  margin: 70px 0 0 70px;
  background: #d9d9d9;
`;

export const Title = styled.div`
  margin: 264px 605px 431px 80px;
  font-weight: 400;
  font-size: 128px;
  line-height: 185px;
  color: #515151d6;
  span {
    transition: opacity 1s ease-in-out;
    opacity: ${(props) => (props.isfading ? "0" : "1")};
    color: ${(props) => (props.titlecount >= 4 ? "#28527A" : "#515151d6")};
  }
`;

export const StartButton = styled.button`
  border: none;
  outline: none;
  cursor: pointer;
  position: absolute;
  right: 50px;
  bottom: 100px;
  width: 331px;
  background: #8ac4d0;
  border-radius: 50px;
  span {
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 32px;
    line-height: 72px;
    color: #515151;
  }
`;
