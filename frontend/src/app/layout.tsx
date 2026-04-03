import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import Sidebar from "@/components/Sidebar";
import TopBar from "@/components/TopBar";

const inter = Inter({ subsets: ["latin"], variable: "--font-inter" });

export const metadata: Metadata = {
  title: "KubeSage AI — DevOps Intelligence Platform",
  description: "Autonomous AI-powered system to monitor, analyze, and self-heal distributed applications.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className={inter.variable}>
      <body className="app-shell">
        <Sidebar />
        <div className="main-area">
          <TopBar />
          <main className="page-content">{children}</main>
        </div>
      </body>
    </html>
  );
}
