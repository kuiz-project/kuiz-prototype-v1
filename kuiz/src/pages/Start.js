import React, { useEffect, useState } from "react";
import { Logo, StartButton, Title, Wrapper } from "./StartStyledComponents";
import { useNavigate } from "react-router-dom";

function Start() {
  const navigate = useNavigate();
  const [titlecount, setTitlecount] = useState(0);
  const [isfading, setIsFading] = useState(false);
  const point = ["연습문제", "해설", "퀴즈", "", "KUIZ"];
  useEffect(() => {
    const timer = setTimeout(() => {
      if (titlecount >= 4) {
        clearTimeout(timer); // KUIZ일때 타이머 멈추기
      } else {
        setIsFading(true); // 숨기기
        setTimeout(() => {
          // 1초 뒤
          setTitlecount((prev) => prev + 1); // 다음 문구 설정
          setIsFading(false); // 보이기(동시에 일어남)
        }, 1000);
      }
    }, 2000);
    return () => clearTimeout(timer);
  }, [titlecount]);

  return (
    <Wrapper>
      <Logo></Logo>
      <Title titlecount={titlecount} isfading={isfading}>
        당신이 원하는 <span>{point[titlecount]}</span>
      </Title>
      <StartButton
        onClick={() => {
          navigate("/home");
        }}
      >
        <span>시작하기</span>
      </StartButton>
    </Wrapper>
  );
}

export default Start;
