import React, { useState } from "react";
import { Document, Page, pdfjs } from "react-pdf";
import { PageContainer, Wrapper } from "./HomeStyledComponents";
pdfjs.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjs.version}/pdf.worker.js`;

function Home() {
  const [file, setFile] = useState(null);
  const [numPages, setNumPages] = useState(null);

  function onDocumentLoadSuccess({ numPages }) {
    if (!numPages) setNumPages(numPages);
  }

  function onFileChange(event) {
    setFile(event.target.files[0]);
    setNumPages(null);
  }

  let content = (
    <div>
      <input type="file" onChange={onFileChange} accept=".pdf" />
    </div>
  );

  if (file) {
    content = (
      <Wrapper>
        <input type="file" onChange={onFileChange} accept=".pdf" />
        <Document
          file={file}
          onLoadSuccess={onDocumentLoadSuccess}
          className={document}
          style={{ border: "2px solid gray" }}
        >
          {Array.from(new Array(numPages), (el, index) => (
            <PageContainer>
              <Page key={`page_${index + 1}`} pageNumber={index + 1} />
            </PageContainer>
          ))}
        </Document>
      </Wrapper>
    );
  }

  return content;
}

export default Home;
