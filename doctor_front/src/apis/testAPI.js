import httpInstance from "@/utils/http.js";

export function getList() {
  return httpInstance({
    url: "/home/category/head",
    // method: "post",
  });
}