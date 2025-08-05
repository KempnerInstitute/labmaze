// Copyright 2016-2019 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//    http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
// ============================================================================

#include "labmaze/cc/char_grid.h"

#include <algorithm>
#include <functional>
#include <string_view>
#include <sstream>

#include "logging.h"

namespace deepmind {
namespace labmaze {

inline std::vector<std::string_view> SplitNonEmptyLines(const std::string& text) {
  std::vector<std::string_view> lines;
  size_t start = 0;
  size_t end = 0;
  while (end != std::string::npos) {
    end = text.find('\n', start);
    size_t length = (end == std::string::npos) ? std::string::npos : end - start;
    std::string_view line = text.substr(start, length);
    if (!line.empty()) {
      lines.push_back(line);
    }
    start = (end == std::string::npos) ? std::string::npos : end + 1;
  }
  return lines;
}

CharGrid::CharGrid(std::string text)
    : raw_data_(std::move(text)),
      rows_(SplitNonEmptyLines(raw_data_)) {
  auto it = std::max_element(rows_.begin(), rows_.end(),
                             [](std::string_view lhs, std::string_view rhs) {
                               return lhs.size() < rhs.size();
                             });
  CHECK(it != rows_.end());
  width_ = it->size();
}

}  // namespace labmaze
}  // namespace deepmind
