import React, { useEffect, useState } from "react";
import { Logo, StartButton, Title, Wrapper } from "./HomeStyledComponents";

function Home() {
  const [titlecount, setTitlecount] = useState(0);
  const [isfading, setIsFading] = useState(false);
  const point = ["연습문제", "해설", "퀴즈", "", "KUIZ"];
  useEffect(() => {
    const timer = setTimeout(() => {
      setIsFading(true);
      setTimeout(() => {
        setTitlecount((prev) => (prev + 1) % point.length);
        setIsFading(false);
      }, 1000);
    }, 2000);
    return () => clearTimeout(timer);
  }, [titlecount]);

  return (
    <Wrapper>
      <Logo></Logo>
      <Title titlecount={titlecount} isfading={isfading}>
        당신이 원하는 <span>{point[titlecount]}</span>
      </Title>
      <StartButton>
        <span>시작하기</span>
      </StartButton>
    </Wrapper>
  );
}

export default Home;
